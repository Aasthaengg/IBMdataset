N, M = map(int, input().split())

if M >= 1:
    S = []
    C = []
    for _ in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
else:
    if N == 3:
        print(100)
    elif N == 2:
        print(10)
    else:
        print(0)
    exit()

ans = [[] for _ in range(N)]

for i in range(M):
    ans[S[i]-1].append(C[i])

ans2 = []

for i in range(len(ans)):
    if len(set(ans[i])) > 1:
        print(-1)
        exit()
    if len(ans[i]) == 0:
        if i == 0:
            ans2.append(1)
        else:
            ans2.append(0)
        continue
    ans2.append(list(set(ans[i]))[0])

if ans2[0] == 0:
    if N == 1:
        print(0)
        exit()
    else:
        print(-1)
        exit()

print(''.join(map(str,ans2)))
    
