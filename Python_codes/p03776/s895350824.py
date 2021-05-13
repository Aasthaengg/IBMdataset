import bisect
import math
N, A, B = map(int, input().split())
v = sorted(list(map(int, input().split())))
ave = sum(v[-A:]) / A
print(ave)
leftA = bisect.bisect_left(v, v[-A])
rightA = bisect.bisect_right(v, v[-A])

def comb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

ans = 0
if v[-A] == v[-1]:
    for i in range(A, min(rightA-leftA, B) + 1):
        ans += comb(rightA-leftA, i)
    print(ans)
else:
    print(comb(rightA-leftA, A+rightA-N))