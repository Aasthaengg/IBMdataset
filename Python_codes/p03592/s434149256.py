N,M,K = map(int,input().split())

for row in range(N+1):
    for colum in range(M+1):
        black = row * M
        black -= row * colum
        black += (N - row) * colum
        if black == K:
            print("Yes")
            exit()

print("No")