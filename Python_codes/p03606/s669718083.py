n = int(input())
ans = []
for i in range(n):
    l,r = map(int,input().split())
    for j in range(l,r+1):
        ans.append(j)

ans = set(ans)

print(len(ans))