n,k=map(int, input().split())
h=[int(x) for x in input().split()]
ans=0
for i in h:
    if k<=i:ans+=1
print(ans)