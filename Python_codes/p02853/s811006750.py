x = [int(i) for i in input().split()]
ans = 0
f = [False,False]
for i in range(2):
    if x[i] == 1:
        ans += 300000
        f[i] = True
    elif x[i] == 2:
        ans += 200000
    elif x[i] == 3:
        ans += 100000

if f[0] and f[1]:
    ans += 400000

print(ans)
