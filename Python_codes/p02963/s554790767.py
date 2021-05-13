s=int(input())

t=int(s**.5)
if t**2>=s:
    t-=1

if t*(t+1)<s:
    x1,y2=t+1,t+1
else:
    x1,y2=t,t+1

x2=x1*y2-s
y1=1

print(0,0,x1,y1,x2,y2)