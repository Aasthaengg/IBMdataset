import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

from collections import deque
N = ri()
a = deque(ri_())
i = 0
cnt = 0
if not 1 in a:
    print(-1)
    exit()
while i < N:
    if a[i] == i + 1:
        i += 1
    else:
        a.popleft()
        N -= 1
        cnt += 1
print(cnt)