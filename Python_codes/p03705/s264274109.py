n,a,b=map(int,input().split())
if a>b or (n==1 and a!=b):
    print(0)
    exit()
if a==b or n==2: print(1)
else:
    print(b*(n-1)+a-a*(n-1)-b+1)