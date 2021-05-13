# B Crane and Turtle
X, Y = map(int, input().split())
for i in range(X+1):
    for j in range(X+1):
        if X * 2 <= Y:
            if Y % 2 == 0:
                if (i * 2) + (j * 2) == Y:
                    print('Yes')
                    exit()
print('No')
