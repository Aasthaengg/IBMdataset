N,M=map(int,input().split())
S=list(input())
S=S[::-1]
ans=[]
P=0
for i in range(1,N+1):
    if P==N:
        break
    for j in range(M+1):
        if P+(M-j)<=N and S[P+(M-j)]=="0":
            ans.append(M-j)
            P+=M-j
            if M-j==0:
                print(-1)
                exit()
            break
ans=ans[::-1]
if 0 in ans:
    print(-1)
else:
    print(*ans)