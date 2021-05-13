N = int(input())
A = list(map(int, input().split()))
A.sort()
m = max(A)
sieve = [True]*(m+1)
sieve[0] = False
ct = 0
for i in range(N):
    n = A[i]
    if sieve[n] == False:
        continue
    if i < N-1 and n == A[i+1]:
        sieve[n] = False
    if sieve[n] == True:
        ct += 1
    for k in range(n*2, m+1, n):
        sieve[k] = False
print(ct)
