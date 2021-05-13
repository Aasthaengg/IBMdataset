h, w = map(int, input().split())
s = []
s.append(["#"] * (w + 2))
for i in range(h):
    s.append(["#"] + list(input()) + ["#"])
s.append(["#"] * (w + 2))

num = [[-1 for i in range(w + 2)] for i in range(h + 2)]
for i in range(1, h + 1):
    l = 0
    m = 0
    while l < w + 2:
        if s[i][l] == "#":
            l += 1
            continue
        else:
            m = l
            while s[i][m] == ".":
                m += 1
            else:
                for j in range(l, m):
                    num[i][j] += m - l
                l = m
for i in range(1, w + 1):
    l = 0
    m = 0
    while l < h + 2:
        if s[l][i] == "#":
            l += 1
            continue
        else:
            m = l
            while s[m][i] == ".":
                m += 1
            else:
                for j in range(l, m):
                    num[j][i] += m - l
                l = m
print(max([max([num[i][j] for j in range(w + 2)]) for i in range(h + 2)]))