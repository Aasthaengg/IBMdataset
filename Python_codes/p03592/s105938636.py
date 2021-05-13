N,M,K=map(int,input().split())
flag=0
for i in range(N+1):
    for j in range(M+1):
        if (N-i)*j+(M-j)*i==K:
            flag=1
            break
if flag==1:
    print("Yes")
else:
    print("No")

