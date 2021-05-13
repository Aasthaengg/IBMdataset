n = int(input())
a = list(map(int ,input().split()))
avg = sum(a) / n
diffs = []
for i in range(n):
    diff = abs(a[i] - avg)
    diffs.append(diff)
minVal = 100
idx = 0
for k in range(n):
    if diffs[k] < minVal:
        minVal = diffs[k]
        idx = k
    else:
        continue
print(idx)