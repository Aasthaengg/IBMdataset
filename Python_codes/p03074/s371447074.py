n, k = map(int, input().split())
s = list(str(input()))

L = []
cur = s[0]
cnt = 0
for i in range(n):
    if s[i] == cur:
        cnt += 1
    else:
        L.append((cnt, int(cur)))
        cnt = 1
        cur = s[i]
else:
    L.append((cnt, int(cur)))

#print(L)

t = 0
S = 0
C = 0
ans = 0
for s in range(len(L)):
    while C <= k and t < len(L):
        if C == k and L[t][1] == 0:
            break
        S += L[t][0]
        if L[t][1] == 0:
            C += 1
        t += 1
    #print(S, C)
    ans = max(ans, S)
    if s == t:
        t += 1
    else:
        S -= L[s][0]
        if L[s][1] == 0:
            C -= 1
print(ans)