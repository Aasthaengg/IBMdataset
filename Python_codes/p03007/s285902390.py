n = int(input())
lis = list(map(int,input().split()))
minus,plus = [],[]
for num in lis:
    if num >= 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
plus.sort()
minus.sort(reverse=True)
ans = []
if len(plus) == 0:
    now = minus.pop(0)
    for num in minus:
        ans.append([now,num])
        now -= num
    print(now)
elif len(minus) == 0:
    now = plus.pop(0)
    last_num = plus.pop(0)
    for num in plus:
        ans.append([now,num])
        now -= num
    ans.append([last_num,now])
    last_num -= now
    print(last_num)
else:
    now = minus.pop(0)
    last_num = plus.pop(0)
    for num in plus:
        ans.append([now,num])
        now -= num
    for num in minus:
        ans.append([last_num,num])
        last_num -= num
    ans.append([last_num,now])
    last_num -= now
    print(last_num)
for i in range(n-1):
    print(*ans[i])