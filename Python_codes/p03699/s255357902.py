n = int(input())
s = list(int(input()) for _ in range(n))
ans = sum(s)
flag = float('inf')
for i in range(n):
    if s[i] % 10 != 0:
        flag = min(flag,s[i])
if ans % 10 == 0:
    if flag != float('inf'):
        print(ans - flag)
    else:
        print(0)
else:
    print(ans)