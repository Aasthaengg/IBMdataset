h, w = map(int, input().split())
s = [input() for _ in range(h)]

neigh = [-1, 0, 1]

for i in range(h):
    for j in range(w):
        cnt = 0
        flag = False
        if s[i][j] == '.':
            for k in neigh:
                for l in neigh:
                    if k==l==0 or i+k < 0 or i+k >= h or j+l < 0 or j+l >= w:
                        continue
                    elif s[i+k][j+l] == '#':
                        cnt += 1
            s[i] = s[i][:j] + str(cnt) +s[i][j+1:]
    print(s[i])
