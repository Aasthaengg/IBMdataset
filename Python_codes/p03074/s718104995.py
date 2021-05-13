n, k = map(int, input().split())
s = str(input())
L = []
cnt = 0
x = '1'
for i in range(n):
    if s[i] == x:
        cnt += 1
    else:
        L.append(cnt)
        x = '0' if x == '1' else '1'
        cnt = 1
else:
    L.append(cnt)
syaku = sum(L[:2*k+1])
ans = syaku
for i in range(len(L)-2*k):
    syaku -= L[i]
    if i % 2:
        syaku += L[i+2*k]
        if i+2*k+1 < len(L):
            syaku += L[i+2*k+1]
    ans = max(ans, syaku)
print(ans)
