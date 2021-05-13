N=int(input())
A=list(map(int,input().split()))
a=1
for i in range(N):
    if A[i]%2==0:
        a*=2
    else:
        a*=1
print(3**N-a)