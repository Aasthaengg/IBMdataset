L = list(map(int, input().split()))

L = sorted(L)
ans = sum(L[:2])
print(ans)