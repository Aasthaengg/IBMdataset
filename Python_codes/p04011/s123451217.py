n=int(input())
k=int(input())
x=int(input())
y=int(input())
s1=k*x
d1=n-k
s2=d1*y

if( k>=n):
    s=x*n
    print(s)
else:
    print(s1+s2)
