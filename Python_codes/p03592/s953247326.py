n, m, k = map(int, input().split())
s = [[0 for i in range(n)]for j in range(m)]
for i in range(n+1):
    for j in range(m+1):
        if (i*m + j*n - 2*i*j) == k:
            print("Yes")
            exit()
print("No")