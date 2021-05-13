a, b, c = map(int, input().split())
x = [a, b, c]
x = sorted(x)
print("Yes" if x[0] + x[1] == x[2] else "No")