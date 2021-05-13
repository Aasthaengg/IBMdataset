def main():
    H, W, N = map(int, input().split())
    s = set()
    for _ in range(N):
        a, b = map(int, input().split())
        s.add((a,b))
    u = set()
    r = [0] * 10
    def search(ii, jj):
        t = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                xt = x + ii
                yt = y + jj
                if (x+ii, y+jj) in s:
                    t += 1
        r[t] += 1
    for t in s:
        for x in range(-1, 2):
            for y in range(-1, 2):
                xt = x + t[0]
                yt = y + t[1]
                if xt < 2 or yt < 2 or xt > H-1 or yt > W-1:
                    continue
                if (xt, yt) in u:
                    continue
                u.add((xt, yt))
                search(xt, yt)
    r[0] = (H-2) * (W-2) - len(u)
    for i in range(10):
        print(r[i])
main()
