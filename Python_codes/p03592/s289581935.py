N,M,K = map(int,input().split())
ans = 'No'
flag = False
for x in range(M+1):
    if flag:
        break
    for y in range(N+1):
        if (N-y)*x+(M-x)*y == K:
            ans = 'Yes'
            flag = True
            break
print(ans)