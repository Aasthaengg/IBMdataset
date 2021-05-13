input()
*l,=map(int,input().split())
ans=0
for i in l:
    for j in l:
        ans+=i*j
print((ans-sum([x*y for (x, y) in zip(l,l)]))//2)