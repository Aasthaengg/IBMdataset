x = int(input())
for i in range(500):
    for j in range(-500, 500):
        if i**5 - j**5 == x:
            print(i,j)
            break
    else:
        continue
    break