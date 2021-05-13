N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

total = 1
s_time = T[0]
count = 1
for i in range(1, N):
    count += 1
    if s_time + K < T[i] or count > C:
        s_time = T[i]
        count = 1
        total += 1
print(total)
