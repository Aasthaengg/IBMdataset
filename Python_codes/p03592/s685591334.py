N,M,K=map(int,input().split())
flag=False

for i in range(N+1):
    for j in range(M+1):
        black= (N-i)*j + (M-j)*i
        if K==black:
            flag=True
            break
    if flag:
        break
       
if flag:
    print("Yes")
else:
    print("No")