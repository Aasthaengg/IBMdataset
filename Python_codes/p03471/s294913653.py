N,Y = map(int,input().split())

for i in range(N+1):
    for j in range(N+1):
        k = N-i-j
        if 1000*i+j*5000+k*10000 == Y and i+j+k == N and k >= 0:
            print(k,j,i)
            exit()
else:
    print(-1,-1,-1)