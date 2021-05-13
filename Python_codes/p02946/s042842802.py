K,X=map(int,input().split())
ans = []
for i in range(-K+1, K):
    ans.append(X+i)
print(*ans)