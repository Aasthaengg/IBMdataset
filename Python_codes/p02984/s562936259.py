N=int(input())
A=list(map(int, input().split())) #ダムの水
#山ダム山ダム山ダム。。。。。
B=[0]*N
A1=0
for i in range(N):
    if i%2==0:
        A1+=A[i]
    else:
        A1-=A[i]
B[0]=A1
for i in range(1,N):
    B[i]=2*A[i-1]-B[i-1]
print(*B)