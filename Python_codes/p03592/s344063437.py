(N,M,K) = map(int,input().split())

for i in range(N+1):
    for j in range(M+1):
        if i*(M-j)+j*(N-i) == K:
            print('Yes')
            flag = 1
            break
        else:
            flag = 0
    if flag == 1:
        break
else:
    print("No")