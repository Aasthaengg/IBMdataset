def abc144_e():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort()
    F.sort(reverse=True)

    low = -1
    up = 10**12
    while up - low > 1:
        v = (up + low) // 2
        tk = K
        for i in range(N):
            tk -= max(0, A[i] - (v // F[i]))
            if tk < 0: break
        if tk < 0:
            low = v
        else:
            up = v
    print(up)

if __name__ == '__main__':
    abc144_e()