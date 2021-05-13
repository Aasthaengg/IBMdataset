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

    for h in hmaps:
        for w in wmaps:
            if (h, w) not in maps:
                print(ans)
                return
    else:
        print(ans-1)


if __name__ == '__main__':
    main()
