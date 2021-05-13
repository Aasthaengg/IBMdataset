import collections

N = int(input())
S = [tuple(sorted(input())) for _ in range(N)]
c = collections.Counter(S)
ans = 0
for i in set(S):
    n = c[i]
    ans += n*(n-1)//2
print(ans)