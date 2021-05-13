n,k,s = map(int,input().split())
ans = []
for i in range(k):
    ans.append(s)
if s < 10**9:
    for i in range(n-k):
        ans.append(s+1)
else:
    for i in range(n-k):
        ans.append(1)
print(" ".join(map(str,ans)))