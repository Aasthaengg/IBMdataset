n = int(input())
if n % 2 != 0:
    print(0)
    exit()

m = 10
a = []
b = []
while m <= n:
    a.append(n // m)
    m *= 5
    if len(a) > 1:
      b.append(a[-2] - a[-1])
if a:
    b.append(a[-1])

ans = 0
for i in range(len(b)):
    ans += (i+1)*b[i]
print(ans)