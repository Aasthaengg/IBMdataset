N=int(input())
A=list(map(int,input().split()))
p=1000000007


R=[0]
G=[0]
B=[0]

#print(A)
ans=1
for i in range(N):
    tmp=0
    if A[i]==R[-1]:
        tmp+=1
    if A[i]==G[-1]:
        tmp+=1
    if A[i]==B[-1]:
        tmp+=1
    ans = (ans*tmp)%p

    if A[i]==R[-1]:
        R.append(R[-1]+1)
        G.append(G[-1])
        B.append(B[-1])
    elif A[i]==G[-1]:
        R.append(R[-1])
        G.append(G[-1]+1)
        B.append(B[-1])
    else:
        R.append(R[-1])
        G.append(G[-1])
        B.append(B[-1]+1)
    
#print(R)
#print(G)
#print(B)
print(ans)