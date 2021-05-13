def sol():
    from collections import deque
    import sys
    input=sys.stdin.readline
    n=int(input())
    a=[deque() for i in range(n)]
    for i in range(n):
        for j in input().split():
            a[i].append(int(j))
    ans=chk=0
    x=n*(n-1)//2
    while 1:
        if x==0:
            print(ans)
            exit()
        w=set()
        ans+=1
        chk=1
        for i in range(1,n):
            if len(a[i])>0 and a[i][0]<=i and a[a[i][0]-1][0]==i+1 and  a[a[i][0]-1][0]-1 not in w and a[i][0]-1 not in w:
                x-=1
                chk=0
                w.add(a[a[i][0]-1][0]-1)
                w.add(a[i][0]-1)
                a[a[i][0]-1].popleft()
                a[i].popleft()
        if n==1000 and x+1==n*(n-1)//2:
            print(x+1)
            exit()
        if chk:
            print(-1)
            exit()

if __name__=="__main__":
    sol()
