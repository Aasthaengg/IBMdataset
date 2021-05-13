abc = list(map(int, input().split()))

ans = sum(abc) - max(abc)
print(ans)