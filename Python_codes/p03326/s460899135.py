import sys
input = sys.stdin.readline

def main():
    N, M = [int(x) for x in input().split()]
    XYZ = [[int(x) for x in input().split()] for _ in range(N)]

    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for x, y, z in XYZ:
            total = 0
            if i >> 0 & 1:
                total += x
            else:
                total -= x
            if i >> 1 & 1:
                total += y
            else:
                total -= y
            if i >> 2 & 1:
                total += z
            else:
                total -= z
            tmp.append(total)

        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))

    print(ans)




if __name__ == '__main__':
    main()


