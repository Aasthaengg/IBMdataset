n,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]
 
ans = 0
for i in range(n):
    if x >= s[i+1]:
        ans = i+1
if x > s[n]:
    ans -= 1
print(ans)