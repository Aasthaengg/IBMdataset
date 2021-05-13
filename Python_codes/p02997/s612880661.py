n,k=map(int,input().split())

#スター型がマックス

if k>((n-1)*(n-2))//2:
    print(-1)
    exit()

ans=set([])

cnt=((n-1)*(n-2))//2
for i in range(2,n+1):
    ans.add((1,i))

for i in range(2,n):
    for j in range(i+1,n+1):
        if cnt>k:
            ans.add((i,j))
            cnt-=1
        else:
            break

print(len(ans))

for item in ans:
    print(item[0],item[1])





