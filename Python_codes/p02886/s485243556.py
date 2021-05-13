n = int(input())
D = list(map(int, input().split()))
pf = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        pf += D[i] * D[j]
print(pf)