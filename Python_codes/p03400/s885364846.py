N = int(input())
D, X = map(int, input().split())

total = X
for _ in range(N):
    A = int(input())
    for _ in range(1, D+1, A):
        total += 1

print(total)