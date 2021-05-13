n = int(input())
s_list = sorted([int(input()) for _ in range(n)])
m = 0
ans = 0
for s in s_list:
    ans += s
    if m == 0 and s % 10 != 0:
        m = s
if m == 0:
    ans = 0
elif ans % 10 == 0:
    ans -= m
print(ans)