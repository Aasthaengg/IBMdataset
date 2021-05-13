w,h,n=map(int,input().split())
a,b,c,d=0,0,w,h
for i in range(n):
 x,y,A=map(int,input().split())
 if A==1:a=max(x,a)
 if A==2:c=min(x,c)
 if A==3:b=max(y,b)
 if A==4:d=min(y,d)
print(max(0,c-a)*max(0,d-b))