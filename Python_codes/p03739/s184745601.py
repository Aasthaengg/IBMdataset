import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())

    # 第一項をプラスにする場合
    r1 = 0
    csum = 0
    parity = True # 「次の項目はプラスであるべき」のTrue/Falseを示す
    for ae in a:
        csum += ae
        if parity:
            if csum <= 0:
                plus = 1 - csum
                r1 += plus
                csum += plus
        else:
            if csum >= 0:
                minus = csum + 1
                r1 += minus
                csum -= minus
        parity ^= 1
    # 第一項をマイナスにする場合
    r2 = 0
    csum = 0
    parity = False
    for ae in a:
        csum += ae
        if parity:
            if csum <= 0:
                plus = 1 - csum
                r2 += plus
                csum += plus
        else:
            if csum >= 0:
                minus = csum + 1
                r2 += minus
                csum -= minus
        parity ^= 1
    print(min(r1, r2))

if __name__ == '__main__':
    main()
