# coding: utf-8
# Your code here!
N=int(input())
A=[0]+list(map(int,input().split()))+[-1]

"""
org_A=A[1:N]

judge=True
for item in org_A:
    if item!=0:
        judge=False
        break
if judge:
    print(N*(N+1)//2)
    exit()
"""

ans=0

wa10=A[1]
wa2=A[1]
front=1
end=0
count=0
while front!=N+1 or end!=N:
    #print(front,end)
    #print(wa10,wa2)
    temp=front-end-1
    if wa10==wa2 and front!=N+1:
        ans+=temp
        front+=1
        wa10+=A[front]
        wa2^=A[front]

    else:
        end+=1
        count=0
        wa10-=A[end]
        wa2^=A[end]
    #print(ans)
    #print("----------------")
print(ans+N)