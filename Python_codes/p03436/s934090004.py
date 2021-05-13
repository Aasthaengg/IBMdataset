from sys import stdin

def main():
    from collections import deque
    import copy
    input = stdin.readline

    h, w = map(int, input().split())
    cm = [[0] * (w + 2) for _ in range(h + 2)]
    que = deque([])
    b = 0
    for i in range(1, h + 1):
        s = input()
        for j in range(1, w + 2):
            if s[j - 1] == ".":
                cm[i][j] = -1
            elif s[j - 1] == "#":
                b += 1
    que.append([1, 1, 0])
    while len(que) > 0:
        y, x, r = que.popleft()
        c = r + 1
        if cm[y + 1][x] == -1:
            cm[y + 1][x] = c
            que.append([y + 1, x, c])
        if cm[y - 1][x] == -1:
            cm[y - 1][x] = c
            que.append([y - 1, x, c])
        if cm[y][x + 1] == -1:
            cm[y][x + 1] = c
            que.append([y, x + 1, c])
        if cm[y][x - 1] == -1:
            cm[y][x - 1] = c
            que.append([y, x - 1, c])
    if cm[h][w] == -1:
        print(-1)
    else:
        print(h * w - b - cm[h][w] - 1)
main()