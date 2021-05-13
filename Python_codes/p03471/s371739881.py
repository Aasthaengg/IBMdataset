N,Y = map(int,input().split())
for i in range(N+1):
    if (Y - 1000*N -9000*i) % 4000 == 0:
        b = (Y - 1000*N -9000*i) // 4000 
        c = N - i - b
        if b >= 0 and c >= 0:
            print(i,b,c)
            exit()
print("-1 -1 -1")