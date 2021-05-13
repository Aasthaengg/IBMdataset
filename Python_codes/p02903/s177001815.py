h, w, a, b = map(int, input().split())

ans = []
for i in range(h):
    tmp = []
    for j in range(w):
        tmp.append(str((1 if i<b else 0)^(1 if j<a else 0)))
    ans.append(tmp)

for l in ans:
    print("".join(l))