N,Y = map(int,input().split())
for i in range(N+1):
    for j in range(N-i+1):
        k = N - j - i
        if 10000 * i + 5000 * j + 1000 * k == Y:
            print(i," ",j," ",k)
            exit()
print(-1,-1,-1)