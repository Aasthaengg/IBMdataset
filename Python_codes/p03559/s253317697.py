import bisect
from itertools import accumulate
n = int(input())
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))
C = sorted(map(int,input().split()))
D = [0]*(n+1)
for i in range(n):
    D[i+1] = n-bisect.bisect_right(C,B[i])
D = tuple(accumulate(D))
ans = 0
for i in range(n):
    j = bisect.bisect_right(B,A[i])
    ans += D[-1]-D[j]
print(ans)