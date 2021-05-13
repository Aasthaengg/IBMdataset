d, n = map(int, input().split())
ans = (100 ** d) * (n if n != 100 else n + 1)
print(ans)
