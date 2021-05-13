n=int(input())

A=list(map(int,input().split()))

B=[]
for i in range(n):
    B.append(A[i]-i-1)

B.sort()

b=B[n//2]

s=0
for i in range(n):
    s+=abs(B[i]-b)

print(s)