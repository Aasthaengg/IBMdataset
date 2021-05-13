N, M = map(int, input().split())
A = [input() for a in range(N)]
B = [input() for b in range(M)]
ans = False
for h in range(N - M + 1):
    for w in range(N - M + 1):
        if ans == True:
            break
        for m in range(M):
            if A[h + m][w:w + M] == B[m]:
                pass
            else:
                ans = False
                break
            ans = True
if ans == True:
    print('Yes')
else:
    print('No')