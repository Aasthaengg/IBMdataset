x,y=map(int,input().split())
count=abs(abs(x)-abs(y))
if x==-y:
    print(1)
elif x*y<0:
    print(count+1)
elif x<y:
    print(count)
elif x*y:
    print(count+2)
else:
    print(count+1)
