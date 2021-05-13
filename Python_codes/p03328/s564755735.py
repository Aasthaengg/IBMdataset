import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    a, b = [int(i) for i in input().strip().split()]
    towers = [0] * 1000
    dif = b - a
    for i in range(1, 1000):
        towers[i] = i + towers[i - 1]
    for i in range(1, 999):
        if towers[i + 1] - towers[i] == dif:
            ans = towers[i + 1] - b
            print(ans)
            break
    return


if __name__ == "__main__":
    main()
