N = int(input())
A1 = [int(a) for a in input().split()]
A2 = [int(a) for a in input().split()]

if N == 1:
    print(A1[0] + A2[0])
    exit()

cum_A1 = [A1[0]] * N
for i in range(1, N):
    cum_A1[i] = cum_A1[i - 1] + A1[i]
cum_A2 = [A2[0]] * N
for i in range(1, N):
    cum_A2[i] = cum_A2[i - 1] + A2[i]

best_total = 0
for down in range(N):
    total = cum_A1[down]
    total += cum_A2[-1]
    if down >= 1:
        total -= cum_A2[down - 1]

    best_total = max(total, best_total)

print(best_total)
