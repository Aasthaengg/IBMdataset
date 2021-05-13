N,M,K = map(int, input().split())

NG_flag = True

for i in range(0,N+1):
    for j in range(0,M+1):
        if i*M + j*N - 2*i*j == K:
            NG_flag = False
            print("Yes")
            break
    
    if NG_flag == False:
        break
else:
    print("No")