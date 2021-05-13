N,M,K = map(int,input().split())
if N==1 or M==1:
    flag = 1
else:
    flag = 0
    for i in range(N+1):
        for j in range(M+1):
            if M*i+N*j-2*i*j==K:
                flag = 1
                break
        if flag==1:break
if flag==1:
    print("Yes")
else:
    print("No")