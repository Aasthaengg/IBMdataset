n, k = map(int, input().split())
A = list(map(int, input().split()))
a = [0] * n
for i in range(n-1):
    for j in range(i+1, n):
        if A[i] > A[j]:
            a[i] += 1

a2 = [0] * n
for i in range(n):
    for j in range(n):
        if A[i] > A[j]:
            a2[i] += 1

print(int(sum(a2)*(k*(k-1)//2) + sum(a)*k) % (10**9+7))