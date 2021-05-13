N, M = map(int, input().split())
A = [list(input()) for i in range(N)]
B = [list(input()) for i in range(M)]
ans = False
for i in range(N-M+1):
    for j in range(N-M+1):
        flag = True
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l] == B[k][l]:
                    continue
                flag = False
                break
            if not flag:
                break
        if flag:
            ans = True
            break
    if ans:
        break
if ans:
    print('Yes')
else:
    print('No')