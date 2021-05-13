x, y = map(int, input().split())
z = [0, 300000, 200000, 100000]

if(x == 1 and y == 1):
    print(1000000)
elif(1 <= x <= 3 and 1 <= y <= 3):
    print(z[x]+z[y])
elif(1 <= x <= 3):
    print(z[x])
elif(1 <= y <= 3):
    print(z[y])
else:
    print(0)