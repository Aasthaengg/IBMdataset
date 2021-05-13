X = int(input())
 
for i in range(1,121):
    for j in range(-121,121+1):
        if i**5 - j**5 == X:
            print(i,j)
            exit()