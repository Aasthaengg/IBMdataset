n, k = map(int, input().split())

l = [0] * (10**5 + 1)

for _ in range(n):
    i, j = map(int, input().split())
    l[i] += j

ind = 0
for i in range(10**5 + 1):
    ind += l[i]
    if ind >= k:
        print(i)
        break