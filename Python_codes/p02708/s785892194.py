n,k = map(int,input().split())
a = list(range(n+1))
b = a[::-1]
ans = 0

min = sum(a[:k-1])
max = sum(b[:k-1])


for i in range(k,n+2):
    min += a[i-1]
    max += b[i-1]
    ele = max - min +1
    ans += ele

M =10**9 + 7
print(ans % M)