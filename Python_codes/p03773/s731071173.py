A, B = map(int, input().split())
x = A + B
print(x if x < 24 else (0 if x == 24 else x - 24))