N = int(input())
K = int(input())
count = 1
for _ in range(N):
    if count <= K:
        count *= 2
    else:
        count += K
print(count)
