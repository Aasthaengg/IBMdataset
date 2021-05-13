n,k = map(int,input().split())
h = [0]*n
for i in range(n):
    h[i] = int(input())

h = sorted(h)
m = 10**10
for i in range(n-k+1):
    m = min(m, h[i+k-1]-h[i])
print(m)