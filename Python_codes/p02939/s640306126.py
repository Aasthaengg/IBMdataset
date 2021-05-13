s = open(0).read().rstrip()
n = len(s)

from collections import defaultdict
ans = defaultdict(int)
ans[-2] = -1
ans[-1] = 0
ans[0] = 1

for i in range(1,n):
    if s[i] != s[i-1]:
        ans[i] = ans[i-1]+1
    else:
        ans[i] = ans[i-3]+2

print(ans[n-1])