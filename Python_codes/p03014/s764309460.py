import sys
input = lambda: sys.stdin.readline().rstrip()


def light_count(light, H, W, h, w, count, wr=-1, hr=-1):

    if wr != -1:
        for i in range(h * W + wr, h * W + w):
            light[i] += count
    elif hr != -1:
        for i in range(hr * W + w, h * W + w, W):
            light[i] += count


def solve():
    H, W = map(int, input().split())
    S = [[] for _ in range(H)]
    light = [0 for _ in range(H * W)]
    for i in range(H):
        S[i] = list(input())

    for h in range(H):
        count = 0
        wr = -1
        for w in range(W):
            if S[h][w] == '.':
                if wr == -1:
                    wr = w
                count += 1
            elif S[h][w] == '#':
                if wr != -1:
                    light_count(light, H, W, h, w, count, wr=wr)
                    wr = -1
                    count = 0
        else:
            if wr != -1:
                light_count(light, H, W, h, w + 1, count, wr=wr)
                wr = -1
                count = 0

    for w in range(W):
        count = 0
        hr = -1
        for h in range(H):
            if S[h][w] == '.':
                if hr == -1:
                    hr = h
                count += 1
            elif S[h][w] == '#':
                if hr != -1:
                    light_count(light, H, W, h, w, count, hr=hr)
                    hr = -1
                    count = 0
        else:
            if hr != -1:
                light_count(light, H, W, h + 1, w, count, hr=hr)
                hr = -1
                count = 0

    print(max(light) - 1)


if __name__ == '__main__':
    solve()
