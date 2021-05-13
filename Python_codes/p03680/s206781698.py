n = int(input())
a = []
for _ in range(n):
    a.append(int(input())-1)

v = [False]*n
v[0] = True

ans = 0
tmp = 0

while tmp != 1:
    ans += 1
    tmp = a[tmp]
    if v[tmp]:
        print(-1)
        exit()
    else:
        v[tmp] = not v[tmp]

print(ans)
