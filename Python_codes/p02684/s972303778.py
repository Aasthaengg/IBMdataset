n,k=map(int,input().split())
a=[-1]+list(map(int,input().split()))
dp=[-1]*(n+1)
now=1
cnt=0
while True:
    nex=a[now]
    cnt+=1
    if dp[nex]!=-1:
        break
    dp[nex]=cnt
    now=nex

loop_start=nex
loop=[loop_start]
loop_now=loop_start
loop_next=-1
while loop_start!=loop_next:
    loop_next=a[loop_now]
    loop.append(loop_next)
    loop_now=loop_next
del loop[-1]
if dp[loop_start]>=k:
    print(dp.index(k))
else:
    d=k-dp[loop_start]
    print(loop[d%len(loop)])
