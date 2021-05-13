balls, colors = map(int,input().split())
ans = colors * ((colors - 1) ** (balls - 1))
print(ans)