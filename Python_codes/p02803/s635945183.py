from sys import stdin

def main():
    from collections import deque
    import copy
    input = stdin.readline

    h, w = map(int, input().split())
    cm = [[0] * (w + 2) for _ in range(h + 2)]
    que = deque([])
    a = deque([])
    for i in range(1, h + 1):
        s = input()
        for j in range(1, w + 2):
            if s[j - 1] == ".":
                cm[i][j] = -1
                a.append([i, j])
    ans = 0
    for b in a:
        dm = copy.deepcopy(cm)
        que.append(b[0])
        que.append(b[1])
        que.append(0)
        dm[b[0]][b[1]] = 0
        while len(que) > 0:
            y = que.popleft()
            x = que.popleft()
            r = que.popleft()
            if ans < r + 1:
                ans = r + 1
            if dm[y + 1][x] == -1:
                dm[y + 1][x] = r + 1
                que.append(y + 1)
                que.append(x)
                que.append(r + 1)
            if dm[y - 1][x] == -1:
                dm[y - 1][x] = r + 1
                que.append(y - 1)
                que.append(x)
                que.append(r + 1)
            if dm[y][x + 1] == -1:
                dm[y][x + 1] = r + 1
                que.append(y)
                que.append(x + 1)
                que.append(r + 1)
            if dm[y][x - 1] == -1:
                dm[y][x - 1] = r + 1
                que.append(y)
                que.append(x - 1)
                que.append(r + 1)
    print(ans - 1)
main()