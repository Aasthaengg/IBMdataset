import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b, c, d, e, f = map(int, input().split())
    a *= 100
    b *= 100

    # 濃度0%のケース
    if e == 0 or min(a, b) == f:
        print(a, 0)
        sys.exit()

    water = [0] * 6001
    water[0] = True
    for i1 in range(3001):
        if water[i1]:
            water[i1 + a] = True
            water[i1 + b] = True
    sugar = [0] * 6001
    sugar[0] = True
    for i1 in range(3001):
        if sugar[i1]:
            sugar[i1 + c] = True
            sugar[i1 + d] = True

    noudo = 0
    r1 = 0
    r2 = 0
    for i1 in range(1, f + 1):
        if water[i1]:
            for i2 in range(f + 1):
                if i1 + i2 > f:
                    break
                if sugar[i2]:
                    if i1 * e >= i2 * 100:
                        if noudo < i2 / (i1 + i2):
                            noudo = i2 / (i1 + i2)
                            r1 = int(i1 + i2)
                            r2 = int(i2)
                    else:
                        break
    if noudo == 0:
        print(a, 0)
    else:
        print(r1, r2)

if __name__ == '__main__':
    main()
