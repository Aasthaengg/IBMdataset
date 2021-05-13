n,a,b = map(int,input().split())

minans = a*(n-1)+b
maxans = a+b*(n-1)

if a>b or (n==1 and a!=b):
    print(0)
else:
    print(maxans-minans+1)