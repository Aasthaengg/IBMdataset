N = int(input())
AAA = list(map(int, input().split()))

AAA.sort()

m = AAA[0]
M = AAA[N-1]

procedures = []
for i in range(1, N-1):
    if AAA[i] > 0:
        procedures.append((m, AAA[i]))
        m -= AAA[i]
    else:
        procedures.append((M, AAA[i]))
        M -= AAA[i]
procedures.append((M, m))

print(M-m)
for x, y in procedures:
    print(x, y)
