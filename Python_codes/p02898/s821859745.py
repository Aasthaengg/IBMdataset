n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

s = 0
for x in h:
    if x >= k:
        s += 1

print(s)