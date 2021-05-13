k = int(input())
n = k//2
if k%2: #odd
    ans = n*(n+1)
else: # even
    ans = n*n

print(ans)
