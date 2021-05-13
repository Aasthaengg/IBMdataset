X,Y = map(int,input().split())
i = X
c = 1
while i < Y:
    i *= 2
    if i <= Y:
        c += 1
print(c)