from collections import Counter

H, W = map(int, input().split())

c = Counter()
for h in range(H):
    c.update(input())

demand2 = W % 2 * (H // 2) + H % 2 * (W // 2)
demand4 = (H // 2) * (W // 2)

supply2 = supply4 = 0
for x in c.values():
    supply4 += x // 4
    supply2 += x % 4 // 2

yes = False
if supply4 >= demand4:
    supply2 += (supply4 - demand4) * 2
    if supply2 >= demand2:
        yes = True

print('Yes' if yes else 'No')