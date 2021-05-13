N = int(input())
b = list(map(int, input().split()))
res = []
for i in range(N):
    for j in range(N-i):
        if b[N-i-j-1] == N-i-j:
            res.append(N-i-j)
            b = b[:N-i-j-1] + b[N-i-j:]
            break
    else:
        print(-1)
        exit()
print(*res[::-1], sep = '\n')