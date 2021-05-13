n,k,s = map(int,input().split())
ans = []
for i in range(k):
    ans.append(s)
if s == 10**9:
    a = 1
else:
    a = s+1
for i in range(n-len(ans)):
    ans.append(a)
print(*ans)