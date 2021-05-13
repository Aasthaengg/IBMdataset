n=int(input())
a,b=map(int,input().split())
for i in range(1,n):
    x,y=map(int,input().split()) 
    if x>=a and y>=b:
        a=x 
        b=y 
        continue 
    mul1=-1 
    mul2=-1 
    if a%x!=0: 
        mul1=a//x  +1 
    else:
        mul1=a//x  
    if b%y==0:
        mul2=b//y 
    else: 
        mul2=b//y+1   
    m=max(mul1,mul2) 
   # print(m,x,y)
    a,b=x*m,y*m   
  #  print(a,b,'gd')
print(a+b)