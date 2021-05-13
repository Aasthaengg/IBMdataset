N = int(input())

H = list(map(int, input().split()))

counts = []
count = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
    else:
        counts.append(count)
        count = 0
else:
    counts.append(count)

print(max(counts))