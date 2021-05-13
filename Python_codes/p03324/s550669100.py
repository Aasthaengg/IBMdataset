D, N = map(int, input().split())

l0 = []
for i in range(1, 102):
    if i != 100:
        l0.append(i)
l1 = []
for i in range(1, 102):
    if i != 100:
        l1.append(100 * i)
l2 = []
for i in range(1, 102):
    if i != 100:
        l2.append(10000 * i)

if D == 0:
    print(l0[N - 1])
elif D == 1:
    print(l1[N - 1])
elif D == 2:
    print(l2[N - 1])
