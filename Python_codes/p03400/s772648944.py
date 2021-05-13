N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

choco = []
for a in A:
    for d in range(100):
        choco.append(a*d+1)

print(len([i for i in choco if i <= D])+X)