n = int(input())
s = [int(input()) for _ in range(n)]

ans = sum(s)
x = []

for i in s:
    if i % 10 != 0:
        x.append(i)
x = sorted(x)

for i in x:
    if ans % 10 == 0:
        ans = ans - i
if ans % 10 == 0:
    print(0)
else:
    print(ans)