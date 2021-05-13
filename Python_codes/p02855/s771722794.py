h, w, k = map(int, input().split())
s = [list(input()) for i in range(h)]
l = [[0] * w for i in range(h + 1)]
c = 1
for i in range(h):
    if "#" in s[i]:
        for j in range(w):
            l[i + 1][j] = c
            if s[i][j] == "#" and "#" in s[i][j + 1:]:
                c += 1
        c += 1
        if l[i][0] == 0:
            m = i
            while l[m][0] == 0:
                l[m] = l[m + 1]
                m -= 1
                if m < 1:
                    break
    else:
        l[i + 1] = l[i]
for i in l[1:]:
    print(*i)