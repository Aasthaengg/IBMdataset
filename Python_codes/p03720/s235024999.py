n, m = map(int, input().split())
NRD = list(0 for i in range(n))
for i in range(m):
    r1, r2 = map(int, input().split())
    NRD[r1 - 1] += 1
    NRD[r2 - 1] += 1
for i in range(n):
    print(NRD[i])