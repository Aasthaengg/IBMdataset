x = int(input())

for i in range(-150, 151):
    for j in range(-150,i):
        if i ** 5 - j ** 5 == x:
            print(i,j)
            exit()