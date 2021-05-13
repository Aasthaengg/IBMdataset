n, m, k = map(int, input().split())

for i in range(n+1):
    for j in range(m+1):
        if i and j:
            ans = i * m + j * n - (i * j * 2)
        elif i > 0 and j == 0:
            ans = i * m
        elif i == 0 and j > 0:
            ans = j * n
        else:
            ans = 0
        if ans == k:
            print('Yes')
            exit()

print('No')