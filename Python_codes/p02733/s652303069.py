import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W, K = [int(x) for x in input().split()]
    S = [list(input().strip()) for _ in range(H)]

    ans = float("inf")

    for n in range(2 ** (H - 1)):
        tmp = 0
        wn = [0] * 10
        wi = [set() for _ in range(10)]

        ni = 0
        for i in range(H):
            wi[ni].add(i)
            if n >> i & 1:
                ni += 1
                tmp += 1

        for i in range(W):
            f = False
            for j in range(H):
                for wii in range(ni + 1):
                    if j in wi[wii]:
                        if wn[wii] + int(S[j][i]) > K:
                            tmp += 1
                            f = True
                        else:
                            wn[wii] += int(S[j][i])
                        break
                if f:
                    break
            if f:
                for wii in range(ni + 1):
                    wn[wii] = 0
                for j in range(H):
                    for wii in range(ni + 1):
                        if j in wi[wii]:
                            wn[wii] += int(S[j][i])
                            break
                for wii in range(ni + 1):
                    if wn[wii] > K:
                        tmp = float("inf")

        ans = min(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
