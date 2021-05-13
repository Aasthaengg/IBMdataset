N=int(input())
A=list(map(int, input().split()))
d = [0]*N
for i in reversed(range(1,N+1)):
    n=1
    t=0
    while i*n<=N:
        t+=d[i*n-1]
        n+=1
    d[i-1]=(t+A[i-1])%2
res = [i+1 for i,x in enumerate(d) if x]
print(len(res))
print(*res)