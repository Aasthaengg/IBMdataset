n = int(input())
V = list(map(int, input().strip().split()))

V.sort()
out = V[0]
for i in range(n - 1):
    j = i + 1
    out = (out + V[j]) / 2
print(out)