import sys
import bisect
input = sys.stdin.readline

n, c, k = [int(w) for w in input().split()]
la = [int(input()) for _ in range(n)]
la.sort()
lak = [a + k for a in la]

ind = 0
ans = 0
while ind < n:
    ride = bisect.bisect_right(la, lak[ind]) - ind
    ind += min(ride, c)
    ans += 1

print(ans)
