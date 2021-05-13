A, B, X = map(int, input().split())
bx = B // X
ax = A // X

if A % X == 0:
    print(bx - ax + 1)
else:
    print(bx - ax)