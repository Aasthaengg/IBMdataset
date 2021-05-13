N=int(input())
A=list(map(int,input().split()))

product=1
div=0

for i in range(N):
    product*=A[i]
for j in range(N):
    div+=product/A[j]

print(product/div)