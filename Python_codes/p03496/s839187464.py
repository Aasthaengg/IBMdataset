N = int(input())
a = list(map(int, input().split()))
mina = min(a)
maxa = max(a)
if mina == maxa:
    print(0)
    exit()

sousa = 0
index = 0
if abs(mina) <= abs(maxa):
    sousa = maxa
    index = a.index(maxa)
else:
    sousa = mina
    index = a.index(mina)

print(2 * N - 1)
for i in range(N):
    print(index + 1, i + 1)

if sousa >= 0:
    for i in range(N - 1):
        print(i + 1, i + 2)
else:
    for i in range(N, 1, -1):
        print(i, i - 1)