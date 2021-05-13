x = int(input())
five = [i**5 for i in range(150)]
for i in range(150):
    for j in range(i+1):
        if five[i] - five[j] == x:
            print(i,j)
            exit()
        if five[i] + five[j] == x:
            print(i,-j)