N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
mx=0
for i in range(N):
    sm=0
    sm+=sum(A[0][0:i+1])+sum(A[1][i:N])
    if sm>mx:
        mx=sm
print(mx)