from collections import Counter
from operator import itemgetter
N = int(input())
A = Counter(map(int, input().split()))
ans = 0
left = 0
for k, v in sorted(A.items(), key=itemgetter(1))[::-1]:
    if left == 1:
        if v == 1:
            ans += 1
            left = 0
            continue
        else:
            v -= 1
            ans += 1
            left = 0
    if v > 3:
        v = v%2 + 2

    if v == 1:
        ans += 1
    elif v == 2:
        left += 1
    elif v == 3:
        ans += 1

print(ans)
