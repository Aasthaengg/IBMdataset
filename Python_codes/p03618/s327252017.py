
A=input()
N=len(A)
D={}
for i in range(N):
    a=A[i]
    if a in D:
        D[a]+=1
    else:
        D[a]=1

#print(D)
ans=N*(N-1)//2
for v in D.values():
    ans-=v*(v-1)//2

print(ans+1)