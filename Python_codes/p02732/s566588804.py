import math

def comb(n):
    if n-2<0:
        return 0
    return math.factorial(n)//(math.factorial(2)*math.factorial(n-2))
    
N=int(input())
A=list(map(int,input().split()))

nums=[0 for i in range(N+1)]
for i in range(N):
    nums[A[i]]+=1

num=0
for i in range(len(nums)):
    num+=comb(nums[i])

for i in range(N):
    ans=num-(nums[A[i]]-1)
    print(ans)