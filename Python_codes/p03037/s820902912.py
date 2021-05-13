n, m = list(map(int, input().split()))

low = 1
high = n

for i in range(m):
    l, r = list(map(int, input().split()))
    low = max(low, l)
    high = min(high, r)

print(max(high - low + 1, 0))

