from math import factorial

N,P=map(int,input().split())
A=list(map(int,input().split()))

num_k=0
num_g=0
for i in range(N):
    if A[i]%2==0:
        num_g+=1
    else:
        num_k+=1

n=num_k//2
ans_k=0
for i in range(0,n*2+1,2):
    ans_k+=factorial(num_k)/factorial(i)/factorial(num_k-i)

ans_g=2**(num_g)

ans=int(ans_k*ans_g)

if P==0:
    print(ans)
else:
    ans=2**N-ans
    print(ans)