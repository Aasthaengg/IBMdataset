X = int(input())

for i in range(1, 360*X+1):
    if((360*i)%X == 0):
        print((360*i)//X)
        break