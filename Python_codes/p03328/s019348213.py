a, b = [int(i) for i in input().split()]

y = b - a

ans = sum(list(range(1, y))) - a
print(ans)
