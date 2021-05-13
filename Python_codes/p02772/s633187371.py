n=int(input())
A=list(map(int,input().split()))
B=[]

for i in range(n):
    if A[i]%2==0:
        B.append(A[i])

cnt=0
for i in range(len(B)):
    if B[i]%3==0 or B[i]%5==0:
        cnt+=1
if cnt==len(B):
    print("APPROVED")
else:
    print("DENIED")