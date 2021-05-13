x, y, z, K = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)


def check(P):
    cnt = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if A[i]+B[j]+C[k] < P:
                    break
                cnt += 1
                if K <= cnt:
                    return True
    return False


L = 1
R = 10**14
while L != R-1:
    M = (L+R)//2
    if check(M):
        L = M
    else:
        R = M

ans = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if A[i]+B[j]+C[k] <= L:
                break
            ans.append(A[i]+B[j]+C[k])

ans.sort(reverse=True)
for i in range(K):
    if i < len(ans):
        print(ans[i])
    else:
        print(L)