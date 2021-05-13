n = int(input())
B = list(map(int,input().split()))
A=[0]*n
A[0]=B[0]
for i in range(n-1):
    if A[i]>B[i]:
        A[i]=B[i]
    A[i+1]=B[i]

t=0
for a in A:
    t+=a
print(t)