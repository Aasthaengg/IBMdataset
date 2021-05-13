N, Y = map(int, input().split())
Y = Y//1000
for a in range(N+1):
    for b in range(N+1-a):
        if Y == a*10 + b*5 + (N - a - b):
            print(a,b,N-a-b)
            exit(0)
else:
    print(-1,-1,-1)