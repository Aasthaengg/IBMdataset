n=int(input())
A=[]
B=[]
C=[]
for i in range(n):
    
    a,b,c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    
dp = [[0,0,0] for i in range(n)]

dp[0] =[A[0],B[0],C[0]]

for i in range(1,n):
    
    a = max(dp[i-1][1], dp[i-1][2]) + A[i]
    b = max(dp[i-1][2], dp[i-1][0]) + B[i]
    c = max(dp[i-1][0], dp[i-1][1]) + C[i]
    
    dp[i] = [a,b,c]
    
print(max(dp[-1]))
