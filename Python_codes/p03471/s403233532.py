N,Y = map(int, input().split())

for j in range(N+1):
    for i in range(N+1):
        sum = 10000*j + 5000*i + 1000*(N-i-j)
        if(sum==Y and N-i-j>=0):
            print(j,i,N-i-j)
            exit()
            
print('-1 -1 -1')