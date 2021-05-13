def resolve():
    n = int(input())
    a = list(map(int, input().split()))

    ll = [0] * 9
    for aa in a:
        if 3200 <= aa:
            ll[0] += 1
            continue
        for i in range(1,9):
            if aa < 400 * i:
                ll[i] += 1
                break
    mn = sum([i > 0 for i in ll[1:]])
    mx = mn + ll[0]
    mn = max(int(ll[0] > 0), mn)

    print(mn, mx)


if __name__ == "__main__":
    resolve()
