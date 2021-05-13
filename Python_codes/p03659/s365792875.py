n = int(input())
a = list(map(int,input().split()))
s = [0]
d = [0]
for i in range(n):
    s.append(s[i]+a[i])
a = list(reversed(a))
for i in range(n):
    d.append(d[i]+a[i])

ans = float('inf')
for i in range(1,n):
    ans = min(ans,abs(s[i]-d[n-i]))
print(ans)