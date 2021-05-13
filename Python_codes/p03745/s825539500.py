n = int(input())
a = list(map(int, input().split()))

l = []
ans = 1
flag = True
for i in range(1, len(a)):
    num = a[i] - a[i - 1]
    if num > 0:
        num = 1
        l.append(num)
    elif num < 0:
        num = -1
        l.append(num)
    else:
        pass
if len(l) > 1:
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            if flag == True:
                ans += 1
                flag = False
            else:
                flag = True
        else:
            flag = True
print(ans)
