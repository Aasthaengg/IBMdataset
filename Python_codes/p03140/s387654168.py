N=int(input())
A=input()
B=input()
C=input()
l=[]
c=0

for i in range(N):
    l=[A[i],B[i],C[i]]
    c=c+len(set(l))-1
print(c)