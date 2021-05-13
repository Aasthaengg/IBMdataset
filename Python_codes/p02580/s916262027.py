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
    mah = max(hc)
    maw = max(wc)
    ans = mah+maw
    hmaps = set()
    wmaps = set()
    for i, h in enumerate(hc):
        if mah == h:
            hmaps.add(i)
    for i, w in enumerate(wc):
        if maw == w:
            wmaps.add(i)

    for h in hmaps:
        for w in wmaps:
            if (h, w) not in maps:
                print(ans)
                return
    else:
        print(ans-1)


if __name__ == '__main__':
    main()
