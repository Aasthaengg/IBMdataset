N=int(input())
q=list(map(int,input().split()))

ans=[]
while q:
    n=len(q)
    for i in range(0,n):
        if q[n-i-1]==n-i:
            ans.append(n-i)
            if i==0:
                q=q[:n-1]
                break
            else:
                q=q[:n-i-1]+q[n-i:]
                break
    else:
        print(-1)
        break
else:
    for i in range(0,N):
        print(ans[-i-1])