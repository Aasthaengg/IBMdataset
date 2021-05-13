n = int(input())

x,y=-1,0
for i in range(n):
    a,b = map(int,input().split())
    if a>x:
        x=a
        y=b

print(x+y)