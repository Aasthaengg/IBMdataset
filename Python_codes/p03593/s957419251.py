from collections import Counter

H, W = map(int, input().split())
S = Counter()
for _ in range(H):
    S.update(list(input()))

val1, val2 = 0, 0
for v in S.values():
    if v % 2:
        val1 += 1
    elif v % 4:
        val2 += 1

val1_lim = 1 if (H % 2 and W % 2) else 0
val2_lim = 0
if H % 2:
    val2_lim += W // 2
if W % 2:
    val2_lim += H // 2

print('Yes' if val1 <= val1_lim and val2 <= val2_lim else 'No')
