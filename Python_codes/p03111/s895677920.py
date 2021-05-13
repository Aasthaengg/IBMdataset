from itertools import product

n, a, b, c = map(int, input().split())
kumiawase = list(product(range(4), repeat=n))
L = []
for _ in range(n):
    L.append(int(input()))


ans = 10 ** 20

for kumi in kumiawase:
    temp = 0
    L0 = []
    L1 = []
    L2 = []
    for j in range(n):
        if kumi[j] == 0:
            L0.append(L[j])
        if kumi[j] == 1:
            L1.append(L[j])
        if kumi[j] == 2:
            L2.append(L[j])
    n0 = len(L0)
    n1 = len(L1)
    n2 = len(L2)
    if n0 == 0 or n1 == 0 or n2 == 0:
        continue
    l0 = sum(L0)
    l1 = sum(L1)
    l2 = sum(L2)
    temp = 10 * (n0 - 1 + n1 - 1 + n2 - 1) + abs(l0 - a) + abs(l1 - b) + abs(l2 - c)
    ans = min(temp, ans)
print(ans)
