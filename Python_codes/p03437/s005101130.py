x,y = [int(i) for i in input().split(" ")]

if x%y == 0:
    print(-1)
    quit()

if x==1:
    print(y*2+1)
    quit()

for i in range(x*2,10**18+1,x):
    if (i < y*2):
        continue
    elif (i%y != 0):
        print(i)
        quit()
print(-1)

