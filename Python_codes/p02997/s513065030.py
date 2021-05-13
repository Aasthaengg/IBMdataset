n,k=map(int,input().split())
ans=set()
for i in range(2,n+1):
    ans.add((1,i))
c=0
import itertools
for x,y in itertools.combinations(list(range(2,n+1)),2):
    if c>=(n-1)*(n-2)//2-k:
        break
    c+=1
    ans.add((x,y))

if (n-1)*(n-2)//2-k<0:
    print(-1)
    exit()
print(len(ans))
for i,j in ans:
    print(i,j)
