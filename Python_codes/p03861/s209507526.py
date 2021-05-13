a,b,x = map(int, input().split())

A=a//x

B=b//x
 
print(B-A+1 if a%x==0  else B-A)