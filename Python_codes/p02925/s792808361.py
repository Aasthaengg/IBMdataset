#!/usr/bin/env python3

def main():
    n = int(input())
    n_prev = [[2 for j in range(n)] for i in range(n)]
    post_matches = [[[] for j in range(n)] for i in range(n)]
    q = []
    for i in range(n):
        ai = list(map(int, input().split()))
        ai = [x - 1 for x in ai]
        for j in range(n - 1):
            x = min(i, ai[j])
            y = max(i, ai[j])
            if j == 0:
                n_prev[x][y] -= 1
                if n_prev[x][y] == 0:
                    q.append((x, y))
            else:
                xp = min(i, ai[j - 1])
                yp = max(i, ai[j - 1])
                post_matches[xp][yp].append((x, y))

    time = 0
    while q:
        time += 1
        qn = []
        while q:
            i, j = q.pop()
            for i2, j2 in post_matches[i][j]:
                n_prev[i2][j2] -= 1
                if n_prev[i2][j2] == 0:
                    qn.append((i2, j2))
        q = qn

    for i in range(n):
        for j in range(i + 1, n):
            if n_prev[i][j] > 0:
                print(-1)
                return
    print(time)

if __name__ == "__main__":
    main()
