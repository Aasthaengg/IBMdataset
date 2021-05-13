n=int(input())

def make_eratosthenes(n):
    A=[0]*(n+1)
    A[0],A[1]=-1,-1 #0と1は対象外
    for i in range(2,n+1):
        if A[i]==0:
            j=i
            while j<n:
                A[j]=i
                j+=i
    return A
E=make_eratosthenes(2000)
P=[]

for i in range(2001):
    if E[i]==i and i%5==1:
        P.append(i)
Ans=[]
for i in range(n):
    Ans.append(P[i])
print(*Ans,sep=" ")