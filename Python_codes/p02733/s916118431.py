h,w,k = map(int,input().split())
s = [list(map(int, input())) for i in range(h)]
ans = h+w-2
for i in range(2**(h-1)):
    index = [0] * h
    rowcuts = 0
    for j in range(h-1):
        if 1 & (i >> j) == 1:
            rowcuts += 1
        index[j + 1] = rowcuts
    chocos = [0] * (rowcuts + 1)
    coulmncuts = 0
    valid = True
    for j in range(w):
        for l in range(h):
            chocos[index[l]] += s[l][j]
        if max(chocos) > k:
            coulmncuts += 1
            chocos = [0] * (rowcuts + 1)
            for l in range(h):
                chocos[index[l]] += s[l][j]
            if max(chocos) > k:
                valid = False
        if not valid:
            break
    if valid:
        ans = min(ans, rowcuts + coulmncuts)

print(ans)