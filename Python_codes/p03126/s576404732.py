N, M = map(int, input().split())
love_count = [0 for _ in range(M)]

for _ in range(N):
    K, *A = input().split()
    for a in A:
        love_count[int(a)-1] += 1

count = 0
for num in love_count:
    if num == N:
        count += 1

print(count)