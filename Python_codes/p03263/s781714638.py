h, w = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(h)]
s = []
for i in range(h):
    for j in range(w-1):
        if m[i][j] & 1:
            s.append("{} {} {} {}".format(i+1, j+1, i+1, j+2))
            m[i][j+1] += 1
for i in range(h-1):
    if m[i][w-1] & 1:
        s.append("{} {} {} {}".format(i+1, w, i+2, w))
        m[i+1][w-1] += 1
print(len(s))
print("\n".join(s))
