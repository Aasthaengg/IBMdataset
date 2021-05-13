N=int(input())
A=list(map(int,input().split()))

K=0
for i in range(N):
    if A[i]%2==0:
        K+=1
print(3**N-2**K)