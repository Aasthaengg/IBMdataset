h,w = map(int,input().split())
s = [0] * h
for i in range(h):
    s[i] = [i for i in str(input())]
ans = [[0] * w for i in range(h)]

for i in range(h):
    box = []
    a = 0
    for j in range(w):
        if s[i][j] == '.':
            box.append(j)
            a += 1
            if j == w-1:
                for k in range(len(box)):
                    ans[i][box[k]] += a
                box = []
                a = 0
        else:
            if j != 0 and len(box) >= 1:
                for k in range(len(box)):
                    ans[i][box[k]] += a
                box = []
                a = 0

for i in range(w):
    box = []
    a = 0
    for j in range(h):
        if s[j][i] == '.':
            box.append(j)
            a += 1
            if j == h-1:
                for k in range(len(box)):
                    ans[box[k]][i] += a
                box = []
                a = 0
        else:
            if j != 0 and len(box) >= 1:
                for k in range(len(box)):
                    ans[box[k]][i] += a
                box = []
                a = 0
aans = 0
for i in range(h):
    aans = max(aans,max(ans[i]))
print(aans-1)

