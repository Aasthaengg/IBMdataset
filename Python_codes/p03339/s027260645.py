n = int(input())
s = list(input())

l = [0]*(n+1)
r = [0]*(n+1)

for i in range(1, n):
    l[i] += l[i-1]
    if s[i-1] == "W":
        l[i] += 1

for i in range(n-1, -1, -1):
    r[i] += r[i+1]
    if s[i] == "W":
        r[i] += 1
        
ans = 1001001001

for i in range(n):
    ans = min(ans, l[i]+(n-i-1-r[i+1]))
    
print(ans)