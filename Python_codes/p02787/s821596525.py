h, n = map(int, input().split())
magic = [list(map(int, input().split())) for _ in range(n)]
hls = [0]
for i in range(h + max(magic, key = lambda x:x[0])[0]):
    pre = []
    for j in range(n):
        hres = i + 1 - magic[j][0]
        if hres >= 0:
            pre.append(hls[hres] + magic[j][1])
        else:
            pre.append(magic[j][1])
    hls.append(min(pre))
print(min(hls[h:]))