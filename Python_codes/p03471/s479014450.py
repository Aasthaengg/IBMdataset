N, Y = map(int,input().split())
for a in range(N+1):
    for b in range(N-a+1):
        if Y == 10000*a + 5000*b + 1000*(N-(a+b)):
            print(a,b,N-(a+b))
            exit(0)
print("-1 -1 -1")
