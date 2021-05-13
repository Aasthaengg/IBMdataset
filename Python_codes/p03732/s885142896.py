def solve(N, W, WVs):
    Ws = {}
    for w, v in WVs:
        Ws.setdefault(w, []).append(v)
    for w, v in Ws.items():
        Ws[w] = sorted(v, key=lambda x: -x)
    wkeys = sorted(Ws.keys())

    m = 0
    for n1 in range(N + 1):
        w1 = n1 * wkeys[0]
        if w1 > W:
            break
        v1 = sum(Ws[wkeys[0]][:n1])
        for n2 in range(N - n1 + 1):
            if len(wkeys) >= 2:
                w2 = n2 * wkeys[1]
                if w1 + w2 > W:
                    break
                v2 = sum(Ws[wkeys[1]][:n2])
            else:
                w2, v2 = 0, 0
            for n3 in range(N - n1 - n2 + 1):
                if len(wkeys) >= 3:
                    w3 = n3 * wkeys[2]
                    if w1 + w2 + w3 > W:
                        break
                    v3 = sum(Ws[wkeys[2]][:n3])
                else:
                    w3, v3 = 0, 0
                for n4 in range(N - n1 - n2 - n3 + 1):
                    if len(wkeys) >= 4:
                        w4 = n4 * wkeys[3]
                        if w1 + w2 + w3 + w4 > W:
                            break
                        v4 = sum(Ws[wkeys[3]][:n4])
                    else:
                        w4, v4 = 0, 0

                    m = max(m, v1 + v2 + v3 + v4)

    return m

if __name__ == "__main__":
    N, W = map(int, input().split(" "))
    WVs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, W, WVs))
