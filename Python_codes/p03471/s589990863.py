N, Y = map(int,input().split())
x, y, z = -1, -1, -1
k = 0
for i in range(N+1):
    for j in range(0,N-i+1):
        k = N - i - j
        if 10000*i + 5000*j + 1000*k == Y and 0 <= k <= 2000:
            x, y, z = i, j, k
            break
print(x, y, z)        