N = int(input())
D, X = [int(a) for a in input().split()]
A = []
for _ in range(N):
    A.append(int(input()))
choco = [0 for _ in range(D)]

for i in range(N):
    day = 1
    j = 0
    while day <= D:
        choco[day-1] += 1
        j += 1
        day = A[i] * j + 1

ans  = sum(choco) + X
print(ans)