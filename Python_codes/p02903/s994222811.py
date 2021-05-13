h, w, a, b = map(int, input().split())

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(str((1 if i<b else 0)^(1 if j<a else 0)))
    print("".join(ans))