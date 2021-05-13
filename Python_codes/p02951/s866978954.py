a, b, c = [int(x) for x in input().split()]
temp = c - (a - b)
ans = temp if temp >= 0 else 0
print(ans)