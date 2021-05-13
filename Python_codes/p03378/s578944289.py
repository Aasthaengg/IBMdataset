n,m,x=map(int,input().split())
a=[int(i) for i in input().split()]
ans1=0
ans2=0
for i in a:
    if i<x:
        ans1+=1
for i in a:
    if i>x:
        ans2+=1

print(min(ans1,ans2))