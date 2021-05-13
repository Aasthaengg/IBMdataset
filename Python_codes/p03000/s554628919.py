n,x=map(int, input().split())
a=[int(x) for x in input().split()]

d=0
ans=0
for i in a:
    d+=i
    if d<=x:ans+=1
print(ans+1)