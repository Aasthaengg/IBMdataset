n,k = map(int,input().split())
h = [int(input()) for _ in range(n)]
h.sort()
m = 10**10
for i in range(n-k+1):
    b = h[i]
    a = h[i+k-1]
    if a - b < m:
        m = a - b

print(m)