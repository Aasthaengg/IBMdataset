n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
x=0
y=0
for i in range(n):
    if x<=a[i][0] and y<=a[i][1]:
        x=a[i][0]
        y=a[i][1]
    else:
        v=-(x//-a[i][0])
        w=-(y//-a[i][1])
        u=max(v,w)
        x=u*a[i][0]
        y=u*a[i][1]

print(x+y)