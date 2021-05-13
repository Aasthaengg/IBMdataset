n = int(input())
p = []
p.append(1)
for i in range(1,n):
    p.append(p[i-1]+i+1)
ans = 0
for i in range(1,n+1):
    ans += i*p[n//i-1]
print(ans)