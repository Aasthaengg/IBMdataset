A, B, C, K = map(int, input().split())

# a = 0a + b + c
# b = 0b + a + c
# c = 0c + a + b
# a - b = - a + b

# a = 2a + b + c
# b = 2b + a + c
# c = 2c + a + b
# a - b = 2a + b + c - 2b - a - c = a - b

# a = 2a + 3b + 3c
# b = 2b + 3a + 3c
# c = 2c + 3a + 3b
# a - b = 2a + 3b + 3c - 2b - 3a - 3c =  - a + b

if abs(A - B) > 1e18:
    print("Unfair")
elif K % 2 == 0:
    print(A - B)
else:
    print(B - A)
