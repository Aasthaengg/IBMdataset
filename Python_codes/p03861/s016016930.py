a, b, x = map(int, input().split(" "))
res = b // x + (1 if a == 0 else -((a - 1) // x))
print(res)
