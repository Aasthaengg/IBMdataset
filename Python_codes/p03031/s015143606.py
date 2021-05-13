import sys
from collections import OrderedDict
input = sys.stdin.buffer.readline

n, m = [int(i) for i in input().split()]
links = OrderedDict()
ans = 0

for i in range(m):
    line = [int(i) for i in input().split()]
    links[i] = line[1:]

conditions = [int(i) for i in input().split()]

switchs = [0] * (n + 1)  # 0:off,1:on
states = [0] * m

for i in range(2**n):
    for j in range(n):
        if (i >> j) & 1:
            switchs[j] = 0
        else:
            switchs[j] = 1
    for i in range(m):
        link = links[i]
        _tmp = 0
        for x in link:
            _tmp += switchs[x - 1]
        if conditions[i] == _tmp % 2:
            states[i] = 1
        else:
            states[i] = 0
    if sum(states) == m:
        ans += 1

print(ans)
