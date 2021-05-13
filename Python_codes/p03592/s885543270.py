h, w, k = map(int, input().split())
for r in range(h + 1):
    for c in range(w + 1):
        s = (h - r) * c + r * (w - c)
        if s == k:
            print('Yes')
            exit()
print('No')
