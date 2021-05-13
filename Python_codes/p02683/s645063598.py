N, M, X = list(map(int, input().split()))
A = []
for i in range(N):
    s = list(map(int, input().split()))
    t = [s[j] for j in range(1, M+1)]
    A.append([s[0], t])
# print(A)

# 下からj番目のbitが1->本jを買う
# B[i]がすべてX以上になればOK
ans = []
for i in range(2**N):
    price = 0
    B = [0]*M
    for j in range(N):
        if (i >> j) & 1:
            price += A[j][0]
            for k in range(M):
                B[k] += A[j][1][k]
    # print(i,[B[k]for k in range(M)])
    for k in range(M):
        if B[k] < X:
            break
    else:
        ans.append(price)

if ans == []:
    print(-1)
else:
    # print(ans)
    print(min(ans))
