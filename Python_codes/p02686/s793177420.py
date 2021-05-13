def check(DR):
    D = 0
    for dr in DR[::-1]:
        dmin, d = dr
        if D + dmin < 0:
            return False
        D += d
    return True

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    DR1 = []
    DR2 = []
    total = 0
    for s in S:
        d = 0    # ["(" の数]  - [")" の数]
        d_min = 0 # ")" が最も深くなるときの ")" の数
        # d_min <= d
        for lr in s:
            if lr == '(':
                d += 1
            else:
                d -= 1
                d_min = min(d, d_min)
        total += d
        if d > 0:
            DR1.append((d_min, d))
        else:
            DR2.append((d_min - d, -d))

    # d_minの大きい順に並べ替える
    DR1.sort()
    DR2.sort()
    if check(DR1) and check(DR2) and sum([d[1] for d in DR1]) == sum([d[1] for d in DR2]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()