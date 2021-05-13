n = int(input())
s = list(map(int,input().split()))
 
maxans = 0
minans = 0
 
color = [0]*8
red = 0
 
for i in s:
    if i>=3200:
        red += 1
    else:
        color[i//400] = 1
        
x = sum(color)
 
if x == 0:
    print(1,red)
else:
    print(x,x+red)