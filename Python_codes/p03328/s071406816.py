a,b=[int(i) for i in input().split()]
sa=b-a
ans=0
for i in range(sa):
    ans+=i
print(ans-a)