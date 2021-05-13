L = list(map(int, input().split()))

ans = 'Yes' if max(L) == (sum(L) - max(L)) else 'No'
print(ans)
