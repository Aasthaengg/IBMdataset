a,b=map(int,input().split())
m=max(a+b,a-b)
m=max(m,a*b)
print(m)