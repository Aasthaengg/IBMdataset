import sys


if __name__ == "__main__":
    n = int(input())
    h = list(map(int,input().split()))
    cnt = 0
    ans = 0
    while True:
        if sum(h) == 0:
            break
        koho = []
        p = []
        for i in range(n):
            if h[i] != 0:
                koho.append(h[i])
            else:
                p.append(koho)
                p.append([0])
                koho = []
        if len(koho)>0:
            p.append(koho)
        for i in range(len(p)):
            if len(p[i]) == 0:
                continue
            d = min(p[i])
            ans += d
            for j in range(len(p[i])):
                p[i][j] -= d
        h = []
        for i in range(len(p)):
            for j in range(len(p[i])):
                h.append(p[i][j])
        cnt += 1
    print(ans)