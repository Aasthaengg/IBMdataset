h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
count = 0
ans = []
for i in range(h):
    for j in range(w-1):
        if a[i][j] % 2 == 1:
            a[i][j+1] += 1
            a[i][j] -= 1
            count += 1
            ans.append([i+1, j+1, i+1, j+2])

for i in range(h-1):
    if a[i][w-1] % 2 == 1:
        a[i+1][w-1] += 1
        a[i][w-1] -= 1
        count += 1
        ans.append([i+1, w, i+2, w])
        
print(count)
for i in range(count):
    print(*ans[i])