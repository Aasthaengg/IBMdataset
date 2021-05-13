N, K = map(int, input().split())
a = sorted([int(x) for x in input().split()])

tot = 0
for i in range(K):
    tot += a[i]
print(tot)
