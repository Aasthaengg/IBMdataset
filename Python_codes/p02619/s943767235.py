d = int(input())
c = list(map(int, input().split()))
csum = 0
for i in range(26):
    csum += c[i]
s = [ [] for _ in range(d)]
for i in range(d):
    s[i] = list(map(int, input().split()))
t = [0 for _ in range(d)]
for i in range(d):
    t[i] = int(input())-1
lastDI = [-1 for _ in range(26)]
ans = 0
for i in range(d):
    ans += s[i][t[i]]
    lastDI[t[i]] = i
    for j in range(26):
        ans = ans - c[j]*(i-lastDI[j])
    print(ans)