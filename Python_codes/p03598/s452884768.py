n=int(input())
k=int(input())
a=[int(i) for i in input().split()]
ans=0

for i in a:
    ans+=min(i*2,(k-i)*2)
print(ans)