N, Y = map(int, input().split())

ans = [-1, -1, -1]

for i in range(0, N+1):
    for j in range(0, (N+1)-i):
        k = N - i - j
        if Y == (10000 * i + 5000 * j + 1000 * k):
            ans = [i, j, k]
    
print(' '.join(map(str, ans)))
