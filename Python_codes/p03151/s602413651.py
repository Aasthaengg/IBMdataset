N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
SA=sum(A)
SB=sum(B)
S=SA-SB
cnt=0
ns=0
if SB>SA:
    print(-1)
    exit()
for a,b in zip(A,B):
    if a>b:
        C.append(a-b)
    elif a<b:
        ns+=b-a
        cnt+=1
C.sort(reverse=True)
for i in range(len(C)):
    if ns>0:
        cnt+=1
        ns-=C[i]
    else:break
print(cnt)