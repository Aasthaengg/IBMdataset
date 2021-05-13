n = int(input())
d = [list(map(int, input().split())) for i in range(n)]
ans = 0
flg = False
for i in d:
    if i[0] == i[1]:
        ans += 1
    else:
        ans = 0
    if ans >= 3:
        flg = True
if flg:
    print("Yes")
else:
    print("No")
