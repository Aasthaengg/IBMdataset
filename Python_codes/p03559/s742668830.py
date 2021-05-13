from itertools import accumulate
import bisect
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
b.sort()
c.sort()
ai = []
bi = []
for i in range(n):
    ai.append(n - bisect.bisect_right(b, a[i]))
    bi.append(n - bisect.bisect_right(c, b[i]))
ans = 0
c = [0]+list(accumulate(bi[::-1]))
for j in ai:
    ans += c[j]
print(ans)