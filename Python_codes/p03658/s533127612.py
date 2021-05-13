n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]

l.sort()
ans=0

for i in range(k):
    ans+=l.pop()
    
print(ans)