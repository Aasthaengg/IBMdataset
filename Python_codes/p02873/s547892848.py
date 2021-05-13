S = input()
L = [0]
for s in S:
    L += [s]
    L += [0]
for i in range(len(L)):
    if L[i] == '<':
        L[i+1] = L[i-1]+1
for i in range(len(L)-1,-1,-1):
    if L[i] == '>':
        L[i-1] = max(L[i-1],L[i+1]+1)
ans = 0
for i in range(len(L)):
    if L[i] not in ['<','>']:
        ans += L[i]
print(ans)