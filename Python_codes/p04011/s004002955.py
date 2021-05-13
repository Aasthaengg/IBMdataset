n,k,x,y=[int(input())for i in range(4)]
a=b=0
a=k*x if n>k else n*x;b=(n-k)*y if n>k else 0
print(a+b)