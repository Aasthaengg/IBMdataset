n = int(input())
a = [int(input()) for _ in range(n)]

a = sorted(a)
tmp = 0
ans = 0
for i in a:
    if i == tmp:
        ans -= 1
        tmp = 0
    else:
        ans += 1
        tmp = i

print(ans)