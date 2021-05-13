from collections import Counter

H, W = map(int, input().split())
X = [input() for _ in range(H)]

ctr = Counter()
for s in X:
    for c in s:
        ctr[c] += 1

if H % 2 == 0 and W % 2 == 0:
    flg1 = all(v % 4 == 0 for v in ctr.values())
    flg2 = True
elif H % 2 == 1 and W % 2 == 1:
    flg1 = sum(v % 2 == 1 for v in ctr.values()) == 1
    flg2 = sum(v % 4 == 2 for v in ctr.values()) <= H // 2 + W // 2
else:
    flg1 = all(v % 2 == 0 for v in ctr.values())
    flg2 = sum(v % 4 == 2 for v in ctr.values()) <= (W // 2 if W % 2 == 0 else H // 2)

if flg1 and flg2:
    print("Yes")
else:
    print("No")
