n, k = map(int, input().split())
h = sorted([int(input()) for x in range(n)])
d = 10**9

for i in range(n-k+1):
    d = min(d, h[i+k-1] - h[i])

    if d == 0:
        break

print(d)
