k = int(input())

p = k // 50
q = k % 50

ansl = [100]*q + [49]*(50-q)
for i in range(50):
    ansl[i] += p - q
print(50)
print(*ansl)
