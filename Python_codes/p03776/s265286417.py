import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
Vs = list(mapint())
Vs.sort(reverse=True)
from collections import defaultdict, Counter
from math import factorial, gcd

count = defaultdict(int)
c = Counter(Vs)
ans = 0
ans_2 = (0, 0)
for i in range(A, B+1):
    val = sum(Vs[:i])
    if val/i>=ans-0.000000000000001:
        ans = val/i
        lowest_cnt = 0
        lowest = Vs[i-1]
        for j in range(i):
            if Vs[j]==lowest:
                lowest_cnt += 1
        val, i = val//gcd(val, i), i//gcd(val, i)
        count[(val, i)] += factorial(c[lowest])/factorial(lowest_cnt)/factorial(c[lowest]-lowest_cnt)
        ans_2 = (val, i)

print(ans)
print(round(count[ans_2]))