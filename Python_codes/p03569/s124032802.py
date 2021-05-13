S = list(input())

notX = []
for s in S:
    if not s == 'x':
        notX.append(s)

if not notX[::-1] == notX:
    print(-1)
    exit()

i = 0
Xcnt = []
cnt = 0
N = len(notX)
for s in S:
    if i < N:
        if s == notX[i]:
            i += 1
            Xcnt.append(cnt)
            cnt = 0
        else:
            cnt += 1

    else:
        cnt += 1

Xcnt.append(cnt)
before = sum(Xcnt)
Xcnt2 = []
N = len(Xcnt)
for i in range(N):
    Xcnt2.append(max(Xcnt[i],Xcnt[N-1-i]))

after = sum(Xcnt2)

print(after-before)
