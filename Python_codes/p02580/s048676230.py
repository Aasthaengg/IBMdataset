import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def main():
    H, W, M = map(int, input().split())
    bombs = []
    hs = [0] * H
    ws = [0] * W
    for _ in range(M):
        h, w = map(int, input().split())
        bombs.append(tuple([h-1, w-1]))
        hs[h-1] += 1
        ws[w-1] += 1
    maxh = max(hs)
    maxw = max(ws)
    ans = maxh + maxw

    maxhindex = [i for i, x in enumerate(hs) if x == maxh]
    maxwindex = [i for i, x in enumerate(ws) if x == maxw]

    bombs = set(bombs)
    for i in maxhindex:
        for j in maxwindex:
            if (i, j) not in bombs:
                print(ans)
                exit()
    print(ans-1)


if __name__ == '__main__':
    main()