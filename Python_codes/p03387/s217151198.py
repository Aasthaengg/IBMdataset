a,b,c=map(int,input().split())
a,b,c=sorted([a,b,c])
d1,d2 = c-a,c-b

if d1==d2:print(d1)
elif (d1-d2)%2==1:print(d2+(d1-d2+1)//2+1)
else:print(d2+(d1-d2)//2)