n = int(input())
ans = []

if n % 2 == 0:
    m = n + 1
else:
    m = n

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i + j != m:
            ans.append([i, j])

print(len(ans))
for i, j in ans:
    print(i, j)
