n, k = map(int, input().split())

L = list(map(int, input().split()))

t = 0
for i in range(n):
    for j in range(i + 1, n):
        if L[i] > L[j]:
            t += 1

t = (t * k) % (10**9 + 7)

L = sorted(L)
s = 0
for i in range(n):
    for j in range(i + 1, n):
        if L[i] < L[j]:
            s += 1
k = k - 1
sum = (k * (k + 1)//2)% (10**9 + 7)
s = (s * sum) % (10**9 + 7)
print((t + s) % (10**9 + 7))