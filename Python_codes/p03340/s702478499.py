N=int(input())
A=[0]+list(map(int,input().split()))+[0]
x=[0]
for i in range(1,2*(10**5+3)):
    x.append(x[-1]+i)
#print(x[:5])
X=0

S=0
E=0
SUM=0
ans=0
for i in range(10**6):
    if S==N+1:
        ans+=x[(S-E-1)]
        break
    if SUM+A[S+1]==SUM^A[S+1]:
        SUM+=A[S+1]
        S+=1
    else:
        ans+=(S-E)
        SUM-=A[E+1]
        E+=1
    #print(ans,S,E,SUM)
print(ans)