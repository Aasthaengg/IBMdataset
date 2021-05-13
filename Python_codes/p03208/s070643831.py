N,K=map(int,input().strip().split())
h=[int(input()) for _ in range(N)]
h.sort()

MIN=h[-1]-h[0]

for n in range(K-1,N):
    MIN=min(MIN,h[n]-h[n-K+1])
print(MIN)