n=int(input())
pt,px,py=0,0,0
for _ in range(n):
    t,x,y=map(int,input().split())
    if t-pt<abs(x-px)+abs(y-py) or (t-pt)%2!=(abs(x-px)+abs(y-py))%2:
        print("No")
        exit()
    pt=t
    px=x
    py=y
print("Yes")