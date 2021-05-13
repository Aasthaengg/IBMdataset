n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

max_j = n - 1
max_diff = r[max_j] - r[max_j - 1]

for i in range(n-3, -1, -1):
    if r[i+1] > r[max_j]:
        max_j = i + 1
    tmp_diff = r[max_j] - r[i]
    if max_diff < tmp_diff:
        max_diff = tmp_diff

print(max_diff)
