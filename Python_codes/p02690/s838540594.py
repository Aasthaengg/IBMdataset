x1=int(input())
for i in range(1,1000):
    x=i**5
    for j in range(-1000,1001):
        if(x-(j**5)==x1):
            print(i,j)
            exit(0)
