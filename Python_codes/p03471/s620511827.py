N,Y = map(int, input().split())
for i in range(0, N+1):
    for j in range(0, N+1-i):
        if i == ((Y - 1000*N - 4000*j) / 9000):
            if (N-i-j) >= 0: print(str(i) + " " + str(j) + " " +str(N-i-j))
            exit()
print ("-1 -1 -1")