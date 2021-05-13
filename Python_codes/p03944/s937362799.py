# vim: fileencoding=utf-8


def main():
    w, h, n = map(int, input().split())
    r = [[0] * h for i in range(w)]
    for i in range(n):
        x, y, a = map(int, input().split())
        if a == 1:
            for j in range(x):
                for k in range(h):
                    r[j][k] = 1
        elif a == 2:
            for j in range(x, w):
                for k in range(h):
                    r[j][k] = 1
        elif a == 3:
            for j in range(w):
                for k in range(y):
                    r[j][k] = 1
        elif a == 4:
            for j in range(w):
                for k in range(y, h):
                    r[j][k] = 1
    ans = 0
    for i in range(w):
        for j in range(h):
            if r[i][j] == 0:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
