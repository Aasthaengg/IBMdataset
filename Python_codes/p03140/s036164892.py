N=int(input())
A=str(input())
B=str(input())
C=str(input())

s = 0
for i in range(N):
    s+=1 if A[i]!=B[i] else 0
    s+=1 if B[i]!=C[i] else 0
    s+=1 if C[i]!=A[i] else 0
    s+=1 if A[i]==B[i] and B[i]==C[i] else 0
    s-=1
print(s)