n,a,b=map(int,input().split())

d=b-a
if d%2==0:
    print(d//2)
else:
    x=min(n-b,a-1)
    print(x+1+(d-1)//2)
