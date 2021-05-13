n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

ans = 'No'
for i in range(n-m+1):
    for j in range(n-m+1):
        match = 1
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] != b[k][l]:
                    match = 0
        if match:
            ans = 'Yes'
print(ans)
