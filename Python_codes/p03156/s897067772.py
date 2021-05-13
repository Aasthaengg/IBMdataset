n=int(input())
a,b=map(int,input().split())
p=sorted(list(map(int,input().split())))
x,y=-1,-1
for i in range(n):
    if x==-1 and p[i]>a:
        x=i
    if y==-1 and p[i]>b:
        y=i
if x==-1 or y==-1:
    print(0)
    exit()
print(min(x,y-x,n-y))