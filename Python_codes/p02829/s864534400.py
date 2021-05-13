A = int(input())
B = int(input())

if (A, B) == (1, 2) or (A, B) == (2, 1):
    print(3)
elif (A, B) == (1, 3) or (A, B) == (3, 1):
    print(2)
else:
    print(1)