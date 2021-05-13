a,b,x=map(int,input().split())
a1=a//x
b1=b//x
print(b1-a1 if a%x!=0 else b1-a1+1)