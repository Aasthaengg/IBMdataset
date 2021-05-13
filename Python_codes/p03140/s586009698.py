N = int(input())
A = list(input())
B = list(input())
C = list(input())
from collections import Counter
ans = 0
for i in range(N):
    da = [A[i],B[i],C[i]]
    c = Counter(da)
    li = list(c.values())
    li.sort()
    ans += 3-li[-1]
print(ans)