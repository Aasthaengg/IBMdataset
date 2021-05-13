def resolve():
    N = int(input())
    C = [[0 for _ in range(10)] for __ in range(10)]
    for i in range(1, N+1):
        c = str(i)
        C[int(c[0])][int(c[-1])] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += C[i][j] * C[j][i]
    print(ans)

if '__main__' == __name__:
    resolve()
