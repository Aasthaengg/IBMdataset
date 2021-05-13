n = int(input())
s = [int(input()) for _ in range(n)]

s.sort()
ac = sum(s)
ans = 0
if ac % 10 != 0:
    ans = ac
else:
    for i in range(n):
        tmp = ac - s[i]
        if tmp % 10 != 0:
            ans = tmp
            break
print(ans)

