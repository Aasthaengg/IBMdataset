import math

DEN=10**9+7
def ret_val(n):
    return n%DEN

N,K=map(int,input().split())

sum=0
for i in range(K,N+2):
    min_val=(i*(i-1))//2
    max_val=i*N-min_val
    sum+=max_val-min_val+1

print(ret_val(sum))