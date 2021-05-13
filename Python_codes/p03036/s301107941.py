li = input().split()
x = int(li[2])
D = int(li[1])
r = int(li[0])

for i in range(0,10,1):
    xx = r*x -D
    print(xx)
    x = xx
