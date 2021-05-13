n = int(input())
a = list(map(int, input().split()))
b = [0]*(n+1)

b[0] = 1
for i in range(n):
    b[i+1] = 2*(b[i] - a[i])

c = [0]*(n+1)
c[n] = a[n]
for j in range(n):
    c[n-1-j] = c[n-j] + a[n-1-j]

d = [0]*(n+1)
flag = 0
for k in range(n+1):
    if b[k] < c[k]:
        d[k] = b[k]
        if d[k] <= 0:
            flag += 1
    else:
        d[k] = c[k]
        if d[k] <= 0:
            flag += 1

ans = sum(d) if flag == 0 else -1
ans = -1 if n == 0 and a[0] > 1 else ans
ans = -1 if a[n] != d[n] else ans
print(ans)