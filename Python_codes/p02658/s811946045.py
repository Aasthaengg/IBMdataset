n = int(input())
a = [int(x) for x in input().split()]

ans = 1

ok = True
for i in range(n):
    ans *= a[i]
    if ans > 10 ** 18:
        ok = False
        break

for i in range(n):
    if a[i] == 0:
        ok = True
        ans = 0

if ok == True:
    print(ans)
else:
    print(-1)