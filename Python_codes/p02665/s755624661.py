from itertools import accumulate
import sys

N = int(input())
A = list(map(int, input().split()))

revA = reversed(A)
ans = 0

l = list(accumulate(revA))
l.reverse()

for i in range(N+1):
    l[i] = min(l[i], 2**i)

for i in range(N+1):
    if i == N:
        if l[i] < A[i]:
            print(-1)
            sys.exit()
    else:
        l[i+1] = min(l[i+1], (l[i]-A[i])*2)

for v in l:
    if v > 0:
        ans += v
    else:
        ans = -1
        break


print(ans)