H, W = [int(i) for i in input().split()]
d = {}
for _ in range(H):
    for a in input():
        if not a in d:
            d[a] = 1
        else:
            d[a] += 1
count = [0, 0, 0, 0, 0]
for v in d.values():
    for i in [4, 2, 1]:
        count[i] += v // i
        v %= i
for i, n in zip([4, 2, 1], [(H // 2) * (W // 2), H % 2 * W // 2 + W % 2 * H // 2, H % 2 * W % 2]):
    if count[i] < n:
        break
    count[i // 2] += (count[i] - n) * 2
else:
    print("Yes")
    exit()
print("No")