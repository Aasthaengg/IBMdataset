from bisect import bisect_left, bisect_right
n,d,a=map(int,input().split())
l=[]
ans=0
for i in range(n):
    x,h=map(int,input().split())
    l.append((x,-(-h//a)))
l.sort()
back=[-1]
rui=[0]
for x,h in l:
    i=bisect_left(back,x)
    h-=rui[-1]-rui[i-1]
    if h<=0:
        continue
    ans+=h
    back.append(x+d*2)
    rui.append(rui[-1]+h)
print(ans)