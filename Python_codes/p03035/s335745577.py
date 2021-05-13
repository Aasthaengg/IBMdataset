a, b = map(int, input().split())
if a >= 13:
    x = b
elif a >= 6:
    x = b / 2
else:
    x = 0
print(int(x))