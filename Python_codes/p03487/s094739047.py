n = int(input())
a = list(map(int,input().split()))
import collections
c = collections.Counter(a)
b = list(set(a))
ans = 0
for N in b:
    if c[N] >= N:
        ans += c[N] - N
    else:
        ans += c[N]
print(ans)