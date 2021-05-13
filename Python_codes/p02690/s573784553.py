X = int(input())
i = 0
f = True
while f:
    for j in range(-i,i+1):
        if i**5 - j**5 == X:
            f = False
            break
    else:
        i += 1
print(i,j)