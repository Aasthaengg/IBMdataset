x,y=map(int,input().split())
a=1
while a!=0:
    a=x%y
    tmp=y
    y=a
    x=tmp
print(tmp)

