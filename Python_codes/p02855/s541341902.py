H,W,K = map(int, input().split())
cnt = 0
ans = []
z = 1
for i in range(H):
    f = list(input())
    if f.count("#") == 0: 
        z += 1
    elif f.count("#") == 1:
        cnt += 1
        row = [cnt] * W
        for i in range(z):
            ans.append(row)
        z = 1
    else:
        _c = 0
        cnt += 1
        row = []
        for j,s in enumerate(f):
            if s == "#":
                if _c == 0:
                    _c += 1
                else:
                    _c += 1
                    cnt += 1
            row.append(cnt)
        for i in range(z):
            ans.append(row)
        z = 1

if z > 1:
    for z in range(z-1):
        ans.append(row)
for i in range(H):
    print(*ans[i])