h=int(input())
w=int(input())
n=int(input())
x=n//h
if n%h!=0:
    x+=1
y=n//w
if n%w!=0:
    y+=1
print(min(x,y))
