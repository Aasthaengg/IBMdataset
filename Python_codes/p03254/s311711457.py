from typing import SupportsComplex


N, x = [int(a) for a in input().split()]
a = [int(a) for a in input().split()]
a = sorted(a)

result = []
for v in a:
    if x >= v:
        result.append(v)
        x -= v
    else:
        break

if len(result) == 0:
    print(0)
    exit()

if (x > 0) and (len(result) == len(a)):
    result[-1] += x

if result[-1] != a[len(result)-1]:
    ans = len(result)-1
else:
    ans = len(result)

print(ans)