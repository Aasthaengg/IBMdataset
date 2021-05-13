N=int(input())
A=input()
B=input()
C=input()
a=0
for i in range(N):
    s=set((A[i],B[i],C[i]))
    a+=len(s)-1
print(a)