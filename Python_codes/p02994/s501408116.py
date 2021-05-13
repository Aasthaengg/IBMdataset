n, l = map(int, input().split())
tastes = [i for i in range(l, l + n)]
ans = sum(tastes) - min(tastes, key=abs)
print(ans)
