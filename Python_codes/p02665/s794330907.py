(N,) = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

numLeafs = A
minNonLeafs = [None for i in range(N + 1)]
maxNonLeafs = [None for i in range(N + 1)]

maxNonLeafs[0] = 1
for i in range(1, N + 1):
    maxNonLeafs[i] = 2 * maxNonLeafs[i - 1] - numLeafs[i]

minNonLeafs[N] = 0
maxNonLeafs[N] = 0
if minNonLeafs[N] + numLeafs[N] > 2 ** N:
    print(-1)
    exit()

for i in range(N - 1, -1, -1):
    minNonLeafs[i] = (minNonLeafs[i + 1] + numLeafs[i + 1] + 1) // 2
    if minNonLeafs[i] + numLeafs[i] > 2 ** i:
        print(-1)
        exit()
    maxNonLeafs[i] = min(maxNonLeafs[i], maxNonLeafs[i + 1] + numLeafs[i + 1])
    if minNonLeafs[i] > maxNonLeafs[i]:
        print(-1)
        exit()

count = 0
for i in range(N + 1):
    count += maxNonLeafs[i] + numLeafs[i]
print(count)
