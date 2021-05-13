def sol():
    n=int(input())+1
    a=[int(i) for i in input().split()]+[2**21-1]
    ans=0
    i=j=w=x=0
    while i<n-1:
        while j<n and w==x:
            w+=a[j]
            x^=a[j]
            j+=1
        ans+=(j-i-1)
        w-=a[i]
        x^=a[i]
        i+=1
    print(ans)

if __name__=="__main__":
    sol()
