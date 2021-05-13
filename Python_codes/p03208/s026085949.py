n,k = map(int,input().split())
h = []
for _ in range(n):
    h.append(int(input()))

h.sort()
ans = float('inf')
for i in range(n-k+1):
    x = h[i+k-1] - h[i]
    if x < ans:
        ans = x

print (ans)
