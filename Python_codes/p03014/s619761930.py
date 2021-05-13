[h,w] = [int(i) for i in input().split()]
s = []
tate = [[0] * (h+2) for i in range(w+2)]
yoko = [[0] * (w+2) for i in range(h+2)]
s.append("#"*(w+2))
for i in range(h):
    tmp = input()
    s.append(tmp.join(["#","#"]))
s.append("#"*(w+2))

#横
for i in range(1,h+1):
    tmp = 1
    before = 1
    while tmp < w+2:
        if s[i][tmp] == "#":
            before += 1
            tmp += 1
        else:
            while s[i][tmp] != "#":
                tmp += 1
                if tmp == w+2:
                    break
            yoko[i][before:tmp] = [tmp-before] * (tmp - before)
            before = tmp

for i in range(1,w+1):
    tmp = 1
    before = 1
    while tmp < h+2:
        if s[tmp][i] == "#":
            before += 1
            tmp += 1
        else:
            while s[tmp][i] != "#":
                tmp += 1
                if tmp == h+2:
                    break
            tate[i][before:tmp] = [tmp-before] * (tmp - before)
            before = tmp
ans = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        ans = max(ans,tate[j][i]+yoko[i][j]-1)
print(ans)
