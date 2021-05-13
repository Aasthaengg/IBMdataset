N = int(input())
s = []
for i in range(N):
    s.append(input())
M = int(input())
t = []
ans = 0
for i in range(M):
    t.append(input())
for i in range(N):
    target = s[i]
    ans = max(ans,s.count(target)-t.count(target))
print(ans)