def main():
    N = int(input())
    inp = [list(map(int, input().split())) for _ in range(N)]

    for cx in range(0, 101):
        for cy in range(0, 101):
            hmax = 10 ** 10
            flg = False
            ha = 0
            for x, y, h in inp:
                m = abs(x-cx) + abs(y-cy)
                if h == 0:
                    hmax = min(hmax, m)
                else:
                    ht = m + h
                    if ht < 1:
                        break
                    if flg:
                        if ht != ha:
                            flg = False
                            break
                    else:
                        flg = True
                        ha = ht
            
            if flg:
                if ha:
                    if ha <= hmax:
                        print(cx, cy, ha)
                        exit()


if __name__ == "__main__":
    main()