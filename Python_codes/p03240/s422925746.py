def main():
    n = int(input())
    H = []
    ans = 0
    X = []
    Y = []
    a = 0
    tmpx = 0
    tmpy = 0
    for _ in range(n):
        x,y,h = map(int,input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
        if h != 0:
            tmpx = x
            tmpy = y
            tmph = h

    for x in range(101):
        for y in range(101):
            flg = True
            h = tmph + abs(x-tmpx) + abs(tmpy-y)
            for i in range(n):
                hh = max(h - abs(x-X[i]) - abs(y - Y[i]), 0)
                if hh != H[i]:
                    flg = False
                    break
            if flg:
                print(x,y,h)
                return
if __name__ == '__main__':
    main()
