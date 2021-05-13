def main():
    H, W, M = (int(i) for i in input().split())
    hc = [0]*(H+1)
    wc = [0]*(W+1)
    maps = set()
    for _ in range(M):
        h, w = (int(i) for i in input().split())
        hc[h] += 1
        wc[w] += 1
        maps.add((h, w))
    mah = -1
    maw = -1
    hmaps = set()
    wmaps = set()
    for i, h in enumerate(hc):
        if mah < h:
            mah = h
            hmaps = {i}
        elif mah == h:
            hmaps.add(i)
    for i, w in enumerate(wc):
        if maw < w:
            maw = w
            wmaps = {i}
        elif maw == w:
            wmaps.add(i)
    ans = mah+maw
    aru = True
    if len(hmaps) * len(wmaps) <= 5*10**6:
        for h in list(hmaps):
            for w in list(wmaps):
                if (h, w) not in maps:
                    aru = False
                    break
    else:
        aru = False
    if aru:
        print(ans - 1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
