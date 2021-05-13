n = int(input())
a = list(map(int, input().split()))


# プラススタート ------------------
ans01 = 0
temp = a[0]
if (temp > 0):
    pass
else:
    add = abs(temp) + 1
    ans01 += add
    temp = 1

for i in range(1, n):
    tar = temp + a[i]
    if (tar * temp < 0):
        temp = tar
    else:
        add = abs(tar) + 1
        ans01 += add
        if (temp > 0):
            temp = -1
        else:
            temp = 1
    #print(tar, ans)
# マイナススタート ------------------
ans02 = 0
temp = a[0]
if (temp < 0):
    pass
else:
    add = abs(temp) + 1
    ans02 += add
    temp = -1

for i in range(1, n):
    tar = temp + a[i]
    if (tar * temp < 0):
        temp = tar
    else:
        add = abs(tar) + 1
        ans02 += add
        if (temp > 0):
            temp = -1
        else:
            temp = 1
    #print(tar, ans)

ans = min(ans01, ans02)

print(ans)
