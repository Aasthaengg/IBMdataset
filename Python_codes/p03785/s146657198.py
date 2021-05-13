n, c, k = map(int, input().split(" "))
t = []
for i in range(n):
    t.append(int(input()))

t.sort()
i = 0
count = 0
while i < n:
    
    j = i + 1
    if i == n - 1:
        count += 1
        break
    while t[j] - t[i] <= k and j < i + c:
        j += 1
        if j == n:
            i = j
            break

    i = j
    count += 1

print(count)