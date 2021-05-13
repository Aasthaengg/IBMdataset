n=int(input())
p=10**9+7
a=pow(10,n,p)
b=pow(9,n,p)
c=pow(8,n,p)
r=a-2*b+c
print(r%p)