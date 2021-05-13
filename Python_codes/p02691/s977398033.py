N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
    L.append(i-A[i])
R = []
for j in range(N):
    R.append(j+A[j])
from collections import Counter
LL = Counter(L)
RR = Counter(R)
ans = 0
for k,v in RR.items():
    ans += v*LL[k]
print(ans)