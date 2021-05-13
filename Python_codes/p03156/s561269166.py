n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))

ans=0
p.sort()
v=0
x=0
z=0
for i in range(len(p)):
    if p[i]<=a:
        v+=1
    elif a<p[i]<=b:
        x+=1
    else:
        z+=1

print(min(v,x,z))