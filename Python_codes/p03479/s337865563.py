x,y = map(int, input().split())

z = y//x 

temp = 1
for i in range(10000):
    temp *= 2
    if z < temp:
        print(i+1)
        exit()