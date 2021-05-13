s=input()
K=int(input())
N=len(s)

A=[]

for i in range(N):
    for j in range(K):
        r=i+j+1
        if r>N:
            break
        A.append(s[i:r])
        
AA=list(set(A))
AA.sort()
print(AA[K-1])


