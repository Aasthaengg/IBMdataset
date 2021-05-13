N = int(input())
A = list(map(int, input().split()))
from collections import Counter
counter = dict(Counter(A))
ans = 0
for num in set(A):
    if counter[num] >= num:
        ans += counter[num] - num
    else:
        ans += counter[num]
print(ans)