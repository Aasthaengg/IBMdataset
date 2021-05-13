import sys
from collections import defaultdict
N = int(input())
if N <= 3:
    print(0)
    sys.exit()
s = input()
ls = [defaultdict(int) for i in range(N)]
a = ['R', 'G', 'B']
for i, x in enumerate(s):
    for y in a:
        if x == y:
            ls[i][y] = ls[max(0, i-1)][y] + 1
        else:
            ls[i][y] = ls[max(0, i-1)][y]
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        if s[i] != s[j]:
            for k in a:
                if k != s[i] and k != s[j]:
                    ans += ls[-1][k] - ls[j][k]
            if 2*j-i <N and s[i] != s[2*j-i] and s[j] != s[2*j-i]:
                ans -= 1
print(ans)
