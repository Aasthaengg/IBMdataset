N,Y = map(int,input().split())
c10000 = 0
for i in range(N+1):
    c1000 = i
    for j in range(N+1-i):
        c5000 = j
        c10000  = N-i-j
        if c1000*1000+ c5000*5000+c10000*10000 == Y:
            print(c10000,c5000,c1000)
            exit()
print(-1,-1,-1)

