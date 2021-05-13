N, Y = map(int, input().split())
ansX = -1
ansY = -1
ansZ = -1
for x in range(N+1):
    for y in range(N+1-x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            ansX = x
            ansY = y
            ansZ = z
            
print(ansX, ansY, ansZ)