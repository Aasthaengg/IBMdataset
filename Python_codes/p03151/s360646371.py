N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
SA=sum(A)
SB=sum(B)
if SA<SB:
    print(-1)
    exit()
ans=0
p=[]
m=[]
for i in range(N):
    a=A[i]-B[i]
    if a>=0:
        p.append(a)
    else:
        m.append(a)
if len(m)==0:
    print(0)
    exit()
M=sum(m)
M=abs(M)
p.sort(reverse=True)
for i in range(len(p)):
    if M<=0:
        break
    ans+=1
    M=M-p[i]
ans+=len(m)
print(ans)