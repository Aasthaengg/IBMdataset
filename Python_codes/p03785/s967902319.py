#AGC011-A Airport Bus
"""
時刻順にソート
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,c,k = map(int,readline().split())
t = []
for i in range(n):
    t.append(int(readline()))

t.sort()
res_k = t[0]
res_c = 0
ans = 0
for i in range(n):
    res_c += 1
    if i+1 < n:
        if t[i+1] - res_k > k:
            ans += 1
            res_c = 0
            res_k = t[i+1]
    if res_c == c:
        ans += 1
        if i+1 < n:
            res_k = t[i+1]
        res_c = 0

print(ans if res_c == 0 else ans + 1)