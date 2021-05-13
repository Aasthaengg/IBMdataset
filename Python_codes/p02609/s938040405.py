def resolve():
    def popcnt(x):
        return bin(x).count("1")

    N = int(input())
    Xs = input()
    X = int(Xs, 2)
    d = popcnt(X)

    lut = [0] * N
    for i in range(1, N):
        Xi = i % popcnt(i)
        lut[i] = lut[Xi] + 1

    dp = d+1
    dm = d-1
    mp = X % dp
    mm = X % dm if dm else 0
    # print(lut)
    # print(format(X, 'b'))

    ans = []
    for i in range(N):
        mask = 1 << (N-i-1)
        Xi = X ^ mask
        _ans = 0
        if Xs[i] == '1':
            if dm:
                m = (mm - pow(2, N-i-1, dm)) % dm
                _ans = lut[m] + 1
            # m = (mm - mask) % dm
        else:
            # m = (mp + mask) % dp
            m = (mp + pow(2, N-i-1, dp)) % dp
            _ans = lut[m] + 1
        ans.append(_ans)
    print(*ans, sep='\n')

resolve()