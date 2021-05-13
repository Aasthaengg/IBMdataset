N = int(input())

L = [2, 1]

for c in range(85):
    Lc = L[-1] + L[-2]
    L.append(Lc)

print(L[N])