n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
ans = sum(a)

i = 0
while ans % 10 == 0:
    if i >= n-1:
        ans = 0
        break
    if a[i] % 10 != 0:
        ans -= a[i]
    i += 1

print(ans)