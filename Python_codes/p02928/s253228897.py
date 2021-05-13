n, k = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7

C1 = [0]*n
C2 = [0]*n

for i in range(n):
    for j in range(n):
        if A[i] > A[j]:
            if j >= i:
                C1[i] += k*(k+1)//2
            else:
                C2[i] += (k-1)*k//2
ans = 0
#print(C1)
#print(C2)
for i in range(n):
    ans += C1[i]+C2[i]
print(ans%mod)
