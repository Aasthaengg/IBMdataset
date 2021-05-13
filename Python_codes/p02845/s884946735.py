N=int(input())
A= list(map(int,input().split()))
B=[0,0,0]
C=1
for i in range(N):
 E=0
 F=0
 for j in range(3):
  if A[i]==B[j]:
   E+=1
   if E==1:
    B[j]+=1
    F=j
 C*=E
 C%=1000000007
print(C)
