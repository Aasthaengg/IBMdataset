n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_time = [0]
b_time = [0]

for i in range(n):
    a_time.append(a_time[-1] + a[i])
for j in range(m):
    b_time.append(b_time[-1] + b[j])

j = m
cnt = 0

for i in range(n+1):
    if a_time[i] > k:
        continue

    while j > 0 and a_time[i] + b_time[j] > k:
        j -= 1
    cnt = max(cnt, i + j)

print(cnt)
