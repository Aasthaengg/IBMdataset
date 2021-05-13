from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    max_i=0
    for i in range(n):
        if abs(a[max_i])<abs(a[i]):
            max_i=i
    
    a=list(map(lambda x:x+a[max_i],a))
    ans=[]
    for i in range(n):
        ans.append([max_i+1,i+1])
    
    if a[0]>=0:
        for i in range(n-1):
            ans.append([i+1,i+2])
    else:
        for i in range(n-1,0,-1):
            ans.append([i+1,i])

    print(2*n-1)
    for i in range(2*n-1):
        print(*ans[i])

if __name__=="__main__":
    main()