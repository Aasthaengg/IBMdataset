A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
a=(10-(A%10))%10
b=(10-(B%10))%10
c=(10-(C%10))%10
d=(10-(D%10))%10
e=(10-(E%10))%10
M=max(a,b,c,d,e)
print(A+a+B+b+C+c+D+d+E+e-M)