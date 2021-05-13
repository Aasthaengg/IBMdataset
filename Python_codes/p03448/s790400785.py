def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    ans = []
    for a in range(A + 1):
        for b in range(B + 1):
            c = (X - 500 * a - 100 * b) / 50
            if c <= C and c >= 0:
                ans.append((a, b, c))

    print((len(set(ans))))

    return

resolve()