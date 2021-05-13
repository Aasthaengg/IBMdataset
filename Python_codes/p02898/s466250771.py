# ABC142
# Roller Coaster
n, k = map(int, input().split())
H = list(map(int, input().split()))
ct = 0
for i in range(n):
    if H[i] >= k:
        ct += 1
print(ct)
