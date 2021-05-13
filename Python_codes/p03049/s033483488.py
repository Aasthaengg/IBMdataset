n = int(input())
lst = [input() for _ in range(n)]

finA = 0
topB = 0
BtoA = 0
cnt = 0
for l in lst:
    cnt += l.count('AB')
    if l[0]=='B' and l[-1]=='A':
        BtoA += 1
    else:
        if l[0]=='B':
            topB += 1
        elif l[-1]=='A':
            finA += 1

if BtoA==0:
    cnt += min(finA, topB)
else:
    if finA==0 and topB==0:
        cnt += BtoA - 1
    else:
        cnt += BtoA + min(finA, topB)
print(cnt)