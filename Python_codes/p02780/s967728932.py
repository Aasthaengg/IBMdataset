import numpy as np
N,K = map(int,input().split())
p = list(map(int,input().split()))

l = []
for i in range(N):
    l.append((1+p[i])/2)

a = [0] * N
a[0] = l[0]
for i in range(1,len(l)):
    a[i] = a[i-1] + l[i]

ans = 0
for i in range(K,len(l)):
    ans = max(ans,a[i]-a[i-K])

if N - K == 0:
    print(max(a))
else:
    print(ans)