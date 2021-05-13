n = int(input())
k = int(input())
p = 1

for i in range(n):
    if p * 2 - p <= k:
        p *= 2
    else:
        p += k

print(p)