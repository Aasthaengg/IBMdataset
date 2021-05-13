h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

# print(s)

d = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]



for i in range(h):
    si = ""
    for j in range(w):
        c = 0
        if s[i][j] == ".":
            for di in d:
                if i+di[0] >= 0 and i+di[0] < h and j+di[1] >= 0 and j+di[1] < w:
                    if s[i+di[0]][j+di[1]] == "#":
                        c += 1
            si += str(c)
        else:
            si += s[i][j]
    s[i] = si

for si in s:
    print(si)
