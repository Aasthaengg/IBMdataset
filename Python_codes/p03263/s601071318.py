import sys
input = sys.stdin.readline

h, w = [int(x) for x in input().split()]
a = []
for _ in range(h):
    a.append([int(x) for x in input().split()])
ans = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if j == w - 1 and i != h - 1:
                if a[i][j] % 2 == 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
            elif a[i][j] % 2 == 1 and j != w - 1:
                a[i][j + 1] += 1
                ans.append([i + 1, j + 1, i + 1, j + 2])
    else:
        for j in range(w - 1, -1, -1):
            if j == 0 and i != h - 1:
                if a[i][j] % 2 == 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
            elif a[i][j] % 2 == 1 and j != 0:
                a[i][j - 1] += 1
                ans.append([i + 1, j + 1, i + 1, j])
print(len(ans))
for i in ans:
    print(*i)
            
