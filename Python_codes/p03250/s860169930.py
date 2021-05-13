a,b,c=map(int,input().split())
x = a+b+c

print(max(max(a,b),c) * 9 + x)