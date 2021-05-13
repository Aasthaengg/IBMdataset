N,M,K = map(int,input().split(" "))
ans = 'No'
for i in range(1,N+1):
    for j in range(1,M+1):
        tmp = i*(M-j)+j*(N-i)
        if tmp == K:
            ans = 'Yes'
            break
        else:continue
    if ans == 'Yes':
        break
if K == N*M or K == 0:
    ans = 'Yes'
print(ans)
