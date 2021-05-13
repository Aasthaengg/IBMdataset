N,Y=map(int,input().split())
for i in range(N+1):
    for j in range(N+1):
        A,B,C=i*10000,j*5000,(N-i-j)*1000
        if A+B+C==Y and i+j+(N-i-j) and -1<N-i-j:
            print(i,j,N-i-j)
            exit()
print(-1,-1,-1)