n = int(input())
a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
ans = 0
c = a[::-1]
d = b[::-1]
for i in range(n):
    ans += (d[i] - (c[i]+ans)%d[i]) % d[i]
print(ans)