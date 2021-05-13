n, k = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))
imax = 100000 * 1000000
imin = 1
while imin < imax:
    imid = (imin + imax) // 2
    track_num = 0
    current = 0
    for i in range(n):
        if w[i] > imid:
            track_num = k
            break
        elif w[i] + current > imid:
            track_num += 1
            current = w[i]
        else:
            current += w[i]
    if track_num < k:
        imax = imid
    else:
        imin = imid + 1
print(imax)