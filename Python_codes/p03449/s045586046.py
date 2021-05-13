N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
L=[A,B]

S=0
for i in range(N):
    K=sum(L[0][0:i+1])+sum(L[1][i:N])
    S=max(S,K)
print(S)