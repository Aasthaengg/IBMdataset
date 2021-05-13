n = int(input())
aas = list(map(int, input().split()))
ms = [-1]*n
ms[0] = 0
for i in range(1,n):
    ms[i] = (aas[i-1] - ms[i-1]/2) * 2
ms[0] = int((ms[0] + (aas[n-1] - ms[n-1]/2) * 2) / 2)
for i in range(1,n):
    ms[i] = int((aas[i-1] - ms[i-1]/2) * 2)
print(*ms)