n,m = map(int,input().split())
a = list(map(int,input().split()))
M = max(a)
a = sorted(a,reverse=True)
t = 0
while M > 1:
    M = -(-M//2)
    t += 1
z = [[] for i in range(t+2)]
for i in range(n):
    s = 0
    b = a[i]
    while b > 1:
        b = -(-b//2)
        s += 1
    z[t-s].append(a[i])
count = 0
for i in range(t+1):
    z[i] = sorted(z[i])
    if count > m:
        break
    while z[i]:
        if count >= m:
            break
        c = z[i].pop()
        z[i+1].append(c//2)
        count += 1
ans = 0
for A in z:
    ans += sum(A)
print(ans)