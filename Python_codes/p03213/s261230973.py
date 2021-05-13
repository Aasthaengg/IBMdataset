import sys

def I(): return int(sys.stdin.readline().rstrip())

N = I()

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

d = {}  # d[p] = Nがpで最大何回割り切れるか
for p in prime:
    r = 0
    for i in range(1,7):
        r += N//(p**i)
    d[p] = r

A = 0  # d[p] >= 74 たるpの個数
B = 0  # d[p] >= 24 たるpの個数
C = 0  # d[p] >= 14 たるpの個数
D = 0  # d[p] >= 4 たるpの個数
E = 0  # d[p] >= 2 たるpの個数

for p in prime:
    if d[p] >= 74:
        A += 1
    if d[p] >= 24:
        B += 1
    if d[p] >= 14:
        C += 1
    if d[p] >= 4:
        D += 1
    if d[p] >= 2:
        E += 1

# 順に、p**74,p**24×q**2,p**14×q**4,p**4×q**4×r**2 の個数を加える

print(A+B*(E-1)+C*(D-1)+((D*(D-1))//2)*(E-2))