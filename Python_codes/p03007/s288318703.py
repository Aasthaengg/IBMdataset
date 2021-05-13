N = int(input())
AAA = list(map(int, input().split()))

AAA.sort()  # 昇順ソート

m = AAA[0]
M = AAA[N-1]
ANS = []

for i in range(1, N-1):
    if AAA[i] > 0:
        ANS.append((m, AAA[i]))
        m -= AAA[i]
        continue
    ANS.append((M, AAA[i]))
    M -= AAA[i]
ANS.append((M, m))

print(M-m)
for (x, y) in ANS:
    print(x, y)
