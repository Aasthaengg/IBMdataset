n,d=map(int,input().split())
x=[]
to=0
for i in range(n):
    x,y=(map(int, input().strip().split()))
    if x**2+y**2<=d*d:
        to+=1
print(to)