N=int(input())
A=list(input())
B=list(input())
C=list(input())
a=0
for i in range(N):
    if A[i]!=B[i] and B[i]!=C[i] and C[i]!=A[i]:
        a+=2
    elif A[i]==B[i] and B[i]==C[i]:
        a+=0
    else:
        a+=1
print(a)