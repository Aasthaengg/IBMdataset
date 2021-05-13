n = int(input())
t, a = map(lambda x: int(x) * 1000, input().split())
h = list(map(lambda x: t - int(x) * 6, input().split()))
print(min(range(n), key=lambda x: abs(h[x]-a)) + 1)
