N = int(input())
T = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    p, x = map(int, input().split())
    total = 0
    for i in range(N):
        if i == p - 1:
            total += x
        else:
            total += T[i]
    print(total)