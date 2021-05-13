def grecom(x,y):
    if(x==0 or y==0):
        return x+y
    if(x==1 or y==1):
        return 1
    if(x==y):
        return x
    if(y>x):
        return grecom(y%x,x)
    else:
        return grecom(x%y,y)

s = input()
a,b=map(int,s.split())
print(grecom(a,b))