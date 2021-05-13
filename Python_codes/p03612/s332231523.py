N = int(input())
P = list(map(int,input().split()))
# print(P)      

ans = 0
for n1 in range(N-1):
    n2 = n1+1
    if P[n1] == n1+1 and P[n2] == n2+1:
        ans+=1
        P[n1],P[n2] = P[n2],P[n1]
        
# print(P,ans)       
for n1 in range(N-1):
    n2 = n1+1
    if P[n1] == n1+1 or P[n2] == n2+1:
        ans+=1
        P[n1],P[n2] = P[n2],P[n1]
        
# print(P)
print(ans)