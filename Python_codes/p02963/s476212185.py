s=int(input())
x1=0
y1=0
x2=10**9
y2=1
y3=s//(10**9)
x3=s%(10**9)
if x3!=0:
    y3+=1
    x3=x2-x3
print(x1,y1,x2,y2,x3,y3)