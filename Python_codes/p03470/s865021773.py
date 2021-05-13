# ABC 085 B - Kagami Mochi
N = int(input())

dn = [0] * N
for i in range(N):
    dn[i] = int(input())

j = N
for i in range(1,101):
    k = dn.count(i)
    if k >= 2:
        j = j - (k - 1)
print(j)