N,M,K = map(int,input().split())

flag = False
for i in range(N+1):
    for j in range(M+1):
        cnt = 0

        cnt += i * M
        cnt += j * N
        cnt -= (i*j)*2

        if cnt == K:
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")