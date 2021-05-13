N=int(input())
l=[]
for i in range(N):
    p=int(input())
    l.append(p)
ans=sum(l)-max(l)//2
print(ans)