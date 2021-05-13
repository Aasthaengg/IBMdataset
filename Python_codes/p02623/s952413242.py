n,m,k = map(int,input().split()) 
Al=list(map(int,input().split()) )
Bl=list(map(int,input().split()) )
bmax=0
A=[0]
B=[0]
for i in range(1,n+1):
    A.append(A[i-1]+Al[i-1])  
for i in range(1,m+1):
    B.append(B[i-1]+Bl[i-1])
    if B[i]<=k:
        bmax=i

ans=0
b=bmax
for a in range(len(A)):
    if A[a]>k:
        break
    # ans = max(ans, a+1)
    
    while A[a] + B[b] >k and b>=0:
        b -= 1
        
        
    ans = max(ans, a+b)
        
print(ans)
