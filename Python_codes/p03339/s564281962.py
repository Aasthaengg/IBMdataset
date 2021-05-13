n = int(input())
s = input()

E = [0]*(n)
eCount = 0
for i in range(n):
    E[i] = eCount
    if s[i] == 'W':
        eCount += 1

W = [0]*n
wCount = 0
for i in range(n-1, -1, -1):
    W[i] = wCount
    if s[i] == 'E':
        wCount += 1

ans = E[0] + W[0]
for i in range(1, n):
    ans = min(ans, E[i]+W[i])

print(ans)