def permutations(L):

    if L == []:
        return [[]]

    else:
        ret = []

        # set（集合）型で重複を削除、ソート
        S = sorted(set(L))

        for i in S:

            data = L[:]
            data.remove(i)

            for j in permutations(data):
                ret.append([i] + j)

        return ret
        

N, M, Q = map(int, input().split())

bou = [1] * N
ball = [2] * (M-1)

junretsu = permutations(bou + ball)

a, b, c, d = [], [], [], []
for i in range(Q):
    A, B, C, D = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)

ans = 0
for i in range(len(junretsu)):
    souwa = 0
    check = 0
    A = []
    for j in range(N+M-1):
        if junretsu[i][j] == 1:
            A.append(j - check + 1)
            check += 1
    for j in range(Q):
        if (A[b[j]-1] - A[a[j]-1]) == c[j]:
            souwa += d[j]
    
    ans = max(ans, souwa)

print(ans)