w,h,x,y=map(int,input().split())
flag=0
if w%2==0 and h%2==0:
  if x == w //2 and y == h // 2:
    flag = 1
s=w*h
print(s/2,flag)
  
