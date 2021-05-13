K,X = map(int,input().split())

l = max(X-K+1,-1000000)
r = min(X+K-1,1000000)

ans = []

for i in range(l,r+1):
    ans.append(str(i))

ans = " ".join(ans)

print(ans)