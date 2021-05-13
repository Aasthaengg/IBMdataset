# ABC155 B - Papers, Please

N =int(input())
A = list(map(int,input().split()))

B=[]
for i in range(len(A)):
    if A[i]%2 ==0:
        B.append(A[i])

if all([B[j]%3==0 or B[j]%5==0  for j in range(len(B))]):
    print('APPROVED')
else:
    print('DENIED')
