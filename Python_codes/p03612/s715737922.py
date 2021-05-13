N = int(input())
p = [0] + list(map(int, input().split()))
count = 0
for i in range(1, N):
    if p[i] == i:
        p[i], p[i + 1] = p[i + 1], p[i]
        count += 1
if p[N] == N:
    print(count + 1)
else:
    print(count)