n, m = map(int, input().split())
keep = [0] * (n + 1)
kep = [-1] * (n + 1)

for i in range(m):
    a = int(input())
    kep[a] = 0
keep[0] = 1
keep[1] = 0 if kep[1] == 0 else 1
for j in range(0, n - 1):
    keep[j + 2] = [0, keep[j] + keep[j + 1]][kep[j + 2]] % 1000000007
print(keep[n])
