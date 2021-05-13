x, a, b = list(map(int, input().split()))
ans = "A" if abs(x-a) < abs(x-b) else "B"
print(ans)
