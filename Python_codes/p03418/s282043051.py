n, k = map(int, input().split())

s = 0
for b in range(1, n+1):
    s += max(0, b-k)*(n//b) + max(0, n%b-k+1)

if k == 0:
    s = n*n
print(s)
