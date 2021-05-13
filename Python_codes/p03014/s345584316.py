h, w = list(map(int, input().split()))
s = [list(map(str, list(input()))) for i in range(h)]  # 文字列の二次元配列入力
yoko = [[] for _ in range(h)]
tate = [[] for _ in range(w)]
for i in range(h):
    cnt = 0
    for j in range(w):
        if j == w-1:
            if s[i][j] == '.':
                cnt += 1
                yoko[i] += [cnt] * (cnt)
            else:
                yoko[i] += [cnt] * (cnt)
                yoko[i].append(0)
        else:
            if s[i][j] == '.':
                cnt += 1
            else:
                yoko[i] += [cnt] * (cnt)
                yoko[i].append(0)
                cnt = 0

for i in range(w):
    cnt = 0
    for j in range(h):
        if j == h-1:
            if s[j][i] == '.':
                cnt += 1
                tate[i] += [cnt] * (cnt)
            else:
                tate[i] += [cnt] * (cnt)
                tate[i].append(0)
        else:
            if s[j][i] == '.':
                cnt += 1
            else:
                tate[i] += [cnt] * (cnt)
                tate[i].append(0)
                cnt = 0

ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans, yoko[i][j]+tate[j][i]-1)
print(ans)
