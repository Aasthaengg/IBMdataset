import functools

n = int(input())
V = sorted(map(int, input().split()))
ans = functools.reduce(lambda x, y: (x + y) / 2, V)
print(ans)