n=int(input())
P=list(map(int,input().split()))
ans=0
M=P[0]
for i in range(n):
    if M>=P[i]:
        ans+=1
        M=P[i]
print(ans)