a, b, c = map(int, input().split())
whole = a + b + c
print("Yes") if (whole / 2) == max([a, b, c]) else print("No")