a, b = map(int, input().split())
l = [i for i in range(1, 1000)]
L = []
for i in range(999):
    L.append(sum(l[:i+1]))


for i in range(998):
    if (L[i] - a) == (L[i+1] - b):
        print(L[i]- a)