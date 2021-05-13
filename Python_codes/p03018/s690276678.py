S = list(input())
N = len(S)
lst = []
l = []
i = 0
while i < N:
    if S[i] == 'A':
        l.append(0)
        i += 1
    elif S[i] == 'B' and i+1 < N and S[i+1] == 'C':
        l.append(1)
        i += 2
    else:
        lst.append(l)
        l = []
        i += 1
if len(l):
    lst.append(l)
ans = 0
for l in lst:
    cnt = 0
    for x in l:
        if x == 0:
            cnt += 1
        else:
            ans += cnt
print(ans)