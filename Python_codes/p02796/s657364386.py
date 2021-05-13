n=int(input())
A=[[] for i in range(n)]
for i in range(n):
    x,l=map(int,input().split())
    A[i]=[x-l,x+l]
A=sorted(A, key=lambda x :x[1])
#print(A)

ans=0
last=-float("INF")
for i in range(n):
    if last<=A[i][0]:
        ans+=1
        last=A[i][1]

print(ans)
