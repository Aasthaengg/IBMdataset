N,M,K = map(int,input().split())
flag = "No"
for i in range(M+1):
    for j in range(N+1):
        if N*i+M*j-2*i*j==K:
            flag = "Yes"
            break
    if flag=="Yes":break
print(flag)