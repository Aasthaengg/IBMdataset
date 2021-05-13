N,K=list(map(int,input().split()))

cnt=0

for b in range(K+1,N+1):
    cnt+=max(0,N//b*(b-K))
    cnt+=max(0,N%b-K+1)

if K>0:
    print(cnt)
else:
    print(N*N)