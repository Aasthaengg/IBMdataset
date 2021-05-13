n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aa = [0]*(n+1)
for i in range(n):
    aa[i+1] = aa[i] + a[i]

bb = [0]*(m+1)
for i in range(m):
    bb[i+1] = bb[i] + b[i]

j = m
ans = 0
for i in range(n+1):
    if aa[i] > k:
        break
    while bb[j] > k-aa[i]:
        j -= 1
    ans = max(ans, i+j)

print(ans)