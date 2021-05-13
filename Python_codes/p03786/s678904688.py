N = int(input())
As = list(map(int, input().split()))
As.sort()
from itertools import accumulate
cum = list(accumulate(As))
cnt = 0
for n in range(N-1):
    if cum[n]*2>=As[n+1]:
        cnt += 1
    else:
        cnt = 0
cnt += 1
print(cnt)