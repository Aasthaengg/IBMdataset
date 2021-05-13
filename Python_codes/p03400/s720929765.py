N = int(input())
D, X = map(int, input().split())

A = [int(input()) for _ in range(N)]

choco = [0] * (D + 1)
for a in A:
    i = 0
    while i * a + 1 <= D:
        choco[i * a + 1] += 1
        i += 1
print(sum(choco) + X)