N = int(input())

ans = 0

L = []
isok = True
for i in range(N):
    n = int(input())
    if n>i: isok = False
    L.append(n)

for i in range(N-1):
    if L[i+1] <= L[i]:
        ans += L[i+1]
    elif L[i+1] == L[i]+1:
        ans += 1
    elif L[i+1] > L[i]:
        isok=False
        break
    
if isok:
    print(ans)
else:
    print(-1)