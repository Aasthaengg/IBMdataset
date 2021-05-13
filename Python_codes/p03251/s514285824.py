n,m,x,y = map(int, input().split())
xlis = list(map(int, input().split()))
ylis = list(map(int, input().split()))

flag = 0

xmax = max(xlis)
ymin = min(ylis)

for i in range(x+1,y+1):
    if i > xmax and i <= ymin:
        flag = 1
        break
    
if flag:
    print("No War")
else:
    print("War")