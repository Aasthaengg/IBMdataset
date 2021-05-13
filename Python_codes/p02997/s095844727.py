n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:
    print(-1)
    exit()
hen=[]
for i in range(1,n):
    for j in range(i+1,n):
        hen.append((i,j))
x=(n-1)*(n-2)//2-k
ans=[(0,i) for i in range(1,n)]
for i in range(x):
    ans.append(hen[i])
print(len(ans))
for x,y in ans:
    print(x+1,y+1)
