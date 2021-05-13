m,k = map(int, input().split())
if k==0:
    ans=[]
    for i in range(2**m):
        ans.append(i)
        ans.append(i)
    print(*ans)
    exit()
if m==1:
    print(-1)
    exit()
if k > 2**m - 1:
    print(-1)
    exit()

ans=[]

for i in range(2**m):
    if i!=k:
        ans.append(i)
ans.append(0)
ans.append(k)
for i in reversed(range(1,2**m)):
    if i!=k:
        ans.append(i)
ans.append(k)

print(*ans)