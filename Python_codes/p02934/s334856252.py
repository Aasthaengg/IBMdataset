n=int(input())
a=[int(i) for i in input().split()]
ans=0.0
d=0
for i in a:
    d=1/i
    ans+=d
print(1/ans)