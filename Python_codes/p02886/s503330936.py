import itertools

N = int(input())
D = tuple(map(int, input().split()))

ans = sum(x * y for x, y in itertools.combinations(D, 2))
print(ans)
