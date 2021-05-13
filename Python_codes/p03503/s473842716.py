n = int(input())

F = [int(input().replace(" ", ""), 2) for _ in range(n)]
P = [list(map(int, input().split())) for _ in range(n)]

answer = -float("inf")
for i in range(1, 2**10):
    temporary = 0
    for j in range(n):
        c = bin(i & F[j]).count("1")
        temporary += P[j][c]
    answer = max(answer, temporary)

print(answer)
