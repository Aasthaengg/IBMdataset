s = str(input())
n = len(s)
cur = s[0]
cnt = 0
L = []
for i in range(n):
    if s[i] != cur:
        L.append(cnt)
        cur = s[i]
        cnt = 1
    else:
        cnt += 1
else:
    L.append(cnt)
#print(L)
print(len(L)-1)
