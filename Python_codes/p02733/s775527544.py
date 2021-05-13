if __name__ == "__main__":
    h, w, k = map(int, input().split())
    s = []

    for _ in range(h):
        si = input()
        s.append(si)
    
    h_split = [0] * (h - 1)
    part = 0
    ans = float('inf')
    for mask in range(1 << (h - 1)):
        g = 0
        g_id = [0] * h
        for i in range(h):
            g_id[i] = g
            if mask >> i & 1 == 1:
                g += 1
        g += 1

        c = []
        for _ in range(g):
            c.append([0] * w)
        
        for i in range(h):
            for j in range(w):
                if s[i][j] == "1":
                    c[g_id[i]][j] += 1
        num = g - 1
        now = [0] * g

        for j in range(w):
            for i in range(g):
                now[i] += c[i][j]
            ok = True
            for i in range(g):
                if now[i] > k:
                    ok = False

            if not ok:
                num += 1
                now = [0] * g
                for i in range(g):
                    now[i] += c[i][j]
                ok = True
                for i in range(g):
                    if now[i] > k:
                        ok = False
                if not ok:
                    num = float('inf')
                    break
        ans = min(ans, num)
    print(ans)