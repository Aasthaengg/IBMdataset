n = int(input())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i],b[i] = map(int,input().split())
a = a[::-1]
b = b[::-1]
ans = 0
for i in range(n):
    if (ans+a[i])%b[i]:
        ans += b[i]-((ans+a[i])%b[i])
print(ans)