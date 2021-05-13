x,y = map(int,input().split())

sa = y-x
tou = 0

for i in range(1,sa):
    tou += i
print(tou-x)