import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

from copy import deepcopy

c = deepcopy(b)

ans = 0

if sum(a) < sum(b):
    print(-1)
    sys.exit()

diff = 0
ad = []

for i, j in zip(a, b):
    if i == j:
        pass
    elif i > j:
        ad.append(i - j)
    else:
        diff += (j - i)
        ans += 1

ad.sort()

while diff > 0:
    diff -= ad.pop()
    ans += 1

print(ans)
        
