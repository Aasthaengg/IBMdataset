N=int(input())
A=list(map(int,input().split()))
t=0
l=1
B=[]
for i in range(N):
    if t==A[i]:
        l+=1
    else:
        B.append(l)
        l=1
        t=A[i]
B.append(l)
ans=0
for i in B:
    ans+=i//2
print(ans)
