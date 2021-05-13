import sys
readline = sys.stdin.readline

N = int(readline())
L = sorted(list(map(int,readline().split())))

# 2本固定すると、もう一本として選べるのは、2本の和より長いものだけ
# これを二分探索で数える

import bisect
ans = 0
for i in range(N - 1):
  for j in range(i + 1,N):
    ans += bisect.bisect_left(L, L[i] + L[j]) - 1 - j
        
print(ans)