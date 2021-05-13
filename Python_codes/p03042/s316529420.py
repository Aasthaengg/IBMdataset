import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

s = readline().rstrip()
a = int(s[:2])
b = int(s[2:])
if 0 < a < 13 and 0 < b < 13:
    ans = "AMBIGUOUS"
elif 0 < a < 13:
    ans = "MMYY"
elif 0 < b < 13:
    ans = "YYMM"
else:
    ans = 'NA'
print(ans)
