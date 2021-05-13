def calcPattern(N, Y):
    for i in range(0, N+1):
        for j in range(0, N+1-i):
            if i == ((Y - 1000*N - 4000*j) / 9000):
                if (N-i-j) >= 0: return (str(i) + " " + str(j) + " " +str(N-i-j))
    return ("-1 -1 -1")
 
n,y = map(int, input().split())
print(calcPattern(n,y))