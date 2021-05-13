N=int(input())
A=input()
B=input()
C=input()
count=N*2
d=0
for i in range(N):
    if A[i]==B[i]==C[i]:
        count += -1
        
    if A[i]==B[i] or A[i]==C[i] or B[i]==C[i]:
        count += -1
        

print(count)