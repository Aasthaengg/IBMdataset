from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    s=readline().strip()

    ans=0
    for i in range(n):
        res=z_algorithm(s[i:])
        for j in range(n-i):
            ans=max(ans,min(res[j],j))

    print(ans)

def z_algorithm(s):
    n=len(s)
    z=[0]*n
    z[0]=n
    i=1
    j=0

    while i<n:
        while i+j<n and s[j]==s[i+j]:
            j+=1
        z[i]=j
        if j==0:
            i+=1
            continue
        k=1
        while i+k<n and k+z[k]<j:
            z[i+k]=z[k]
            k+=1
        i+=k
        j-=k
    return z

if __name__=="__main__":
    main()