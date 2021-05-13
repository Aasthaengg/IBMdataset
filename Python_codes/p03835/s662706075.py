k, s = map(int, input().split())

count = 0
for i in range(k+1):
    for j in range(k+1):
        if i + j > s:
            break
        m = s - i - j
        if m <= k:
            count += 1
print(count)