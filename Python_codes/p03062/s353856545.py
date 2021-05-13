n = int(input())
a = list(map(int, input().split()))
c = 0
m = 10**10
flag = 0
ans = 0
for i in a:
    if i == 0:
        flag = 1
    if i < 0:
        c += 1
    ans += abs(i)
    m = min(m,abs(i))
if c%2 == 0:
    flag = 1
if flag:
    print(ans)
else:
    print(ans-(2*m))

