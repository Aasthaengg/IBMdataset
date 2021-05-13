N, M = map(int, input().split())
B = [0 for _ in range(M+1)]

for i in range(N):
    KA = list(map(int, input().split()))
    for a in KA[1:]:
        B[a] += 1
count = 0
for b in B:
    if b == N:
        count += 1
print(count)
