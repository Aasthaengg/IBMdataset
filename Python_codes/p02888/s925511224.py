import itertools, bisect

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i, j in itertools.combinations(range(N), 2):
    ans += bisect.bisect_left(L, L[i] + L[j]) - j - 1
print(ans)
