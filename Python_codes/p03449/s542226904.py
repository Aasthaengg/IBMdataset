n = int(input())
A = [list(map(int,input().split())) for i in range(2)]

b=0
ans=0

for j in range(n):
    
    b = sum(A[0][0:j+1])+sum(A[1][j:])
    ans =max(b,ans)

print(ans)