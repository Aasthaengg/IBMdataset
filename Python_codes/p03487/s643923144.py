n = int(input())
a = list(map(int, input().split()))
import collections
a = collections.Counter(a)
ans = 0
for i,j in a.items():
    if i>j:
        ans += j
    else:
        ans += abs(i-j)
print(ans)
