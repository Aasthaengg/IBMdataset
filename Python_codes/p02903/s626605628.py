h, w, a, b = map(int, input().split())

ans = []
for i in range(h):
    tmp = []
    if i < b:
        x = 0
    else:
        x = 1
    for j in range(w):
        if j < a:
            y = 0
            tmp.append(str(x^y))
        else:
            y = 1
            tmp.append(str(x^y))
    ans.append(tmp)

for l in ans:
    print("".join(l))