n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

ah = len(a)
aw = len(a[0])
bh = len(b)
bw = len(b[0])

for i in range(ah - bh + 1):
    for j in range(aw - bw + 1):
        tmp = []
        for k in range(bh):
            tmp.append(a[i + k][j : j + bw])
        if b == tmp:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")