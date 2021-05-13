N = int(input())
s = [(input()) for _ in range(N)] + ['0']
M = int(input())
t = [(input()) for _ in range(M)]
s.sort(reverse=True)
sc = 0
ans = 0
for i in range(N) :
    sc += 1
    if s[i] == s[i+1] :
        continue
    tc = t.count(s[i])
    ans = max(ans,sc-tc)
    sc = 0

print(ans)