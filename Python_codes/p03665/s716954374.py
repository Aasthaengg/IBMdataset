n, p = map(int, input().split()); a = list(map(int, input().split()))
s = t = u = 0; b = [1]
for i in range(n):
    if a[i]%2 == 0: s += 1
    else: t += 1
for i in range(1, n+1):
    b.append(b[-1]*i)
if p == 0:
    for i in range(0, t//2*2+1, 2):
        u += b[t]//b[i]//b[t-i]
else:
    for i in range(1, (t+1)//2*2, 2):
        u += b[t]//b[i]//b[t-i]
print(2**s*u)