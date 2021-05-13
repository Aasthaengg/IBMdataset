h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    count = 0
    start = 0
    end = 0
    for j in range(w):
        if s[i][j] != "#":  # 　#じゃなければおけ
            count += 1
        else:
            for z in range(start, end):
                s[i][z] = count
            start = end+1
            count = 0
        end += 1
    for z in range(start, end):
        s[i][z] = count
    # print(s[i])
ans = 0

for i in range(w):
    count = 0
    start = 0
    end = 0
    for j in range(h):
        if s[j][i] != "#":  # 　#じゃなければおけ
            count += 1
        else:
            for z in range(start, end):
                s[z][i] += count
            start = end+1
            count = 0
        end += 1
    for z in range(start, end):
        s[z][i] += count
# print()
for i in range(h):
    # print(s[i])
    for j in range(w):

        if s[i][j] != "#":
            ans = max(ans, s[i][j])
print(ans-1)
