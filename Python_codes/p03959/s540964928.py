n = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
mod = 10**9+7
if max(A)!=max(T):
    print(0)
    exit()
l = [True] + [False]*(n-1)
r = [False]*(n-1) + [True]

for i in range(1, n):
    if T[i] != T[i-1]:
        l[i] = True
for i in range(n-1):
    if A[i] != A[i+1]:
        r[i] = True
for i in range(n):
    if r[i] and A[i]>T[i]:
        print(0)
        exit()       
ans = 1
for i in range(n):
    if l[i]==False and r[i]==False:
        ans *= min(T[i], A[i])
        ans %= mod
print(ans%mod)