import collections
N = int(input())
num = []
mod = 10**9+7
for i in range(2,N+1):
    for j in range(2,i+1):
        #print(j)
        while i%j==0:
            i //= j
            num.append(j)
#print(num)
A = collections.Counter(num)
#print(A)
ans = 1
for v in A.values():
    ans *= (v+1)%mod
print(ans%mod)