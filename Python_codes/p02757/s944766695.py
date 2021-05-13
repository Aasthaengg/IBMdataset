import sys


N,P = map(int,input().split())
S = list(input())

A = [0]*(N)
A[-1] = int(S[-1])
A[-1] %= P
base = 10 % P
for i in reversed(range(N-1)):
    A[i] = A[i+1] + base*int(S[i])
    A[i] %= P
    base *= 10
    base %= P


ans = 0
if P==2 or P==5:
    for i in reversed(range(N)):
        if int(S[i])%P==0:
            ans += i+1
else:
    nums = {}
    for a in A:
        if not (a in nums):
            nums[a] = 1
        else:
            nums[a] += 1
    
    for n in nums.keys():
        k = nums[n]
        if n==0:
            ans += k*(k+1)//2
        else:
            ans += k*(k-1)//2
    
print(ans)    

