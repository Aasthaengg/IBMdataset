h, w = map(int, input().split())
lst = []
for i in range(h):
    lsti = list(map(int, input().split()))
    lst.append(lsti)

num = 0
ans = []
for i in range(h-1):
    for j in range(w):
        if lst[i][j] % 2 == 1:
            lst[i][j] -= 1
            lst[i+1][j] += 1
            num += 1
            ans.append([i+1, j+1, i+2, j+1])

for j in range(w-1):
    if lst[h-1][j] % 2 == 1:
        lst[h-1][j] -= 1
        lst[h-1][j+1] += 1
        num += 1
        ans.append([h, j+1, h, j+2])

print(num)
for i in range(num):
    ansi = ans[i]
    print(ansi[0], ansi[1], ansi[2], ansi[3])