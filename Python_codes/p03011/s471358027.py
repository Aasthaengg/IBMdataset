a,b,c=map(int,input().split())
k=a+b+c
print(k-max(max(a,b),c))