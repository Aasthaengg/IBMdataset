def cz(A):
    N = len(A)
    F = [0]
    for i in range(N):
        if A[i] == 0:
            F.append(0)
        else:
            F.append(1)

    res = 0
    for i in range(N):
        if F[i] == 0 and F[i+1] == 1:
            res += 1

    return(res)

N = int(input())
H = list(map(int,input().split()))

cnt = 0
while sum(H) > 0:
    cnt += cz(H)
    for i in range(N):
        if H[i] == 0:
            continue
        else:
            H[i] -= 1

print(cnt)
