import itertools
N=int(input())
A=list(map(int,input().split()))
all=pow(3,N)
sub=1

for i in range(N):
    if A[i]%2==0:
        sub=sub*2
    else:
        sub=sub
print(all-sub)

