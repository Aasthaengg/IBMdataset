a,b=map(int,input().split())
x=(a+b)%2
if x==1 :
    y=(a+b+1)//2
else :
    y=(a+b)//2
print(y)