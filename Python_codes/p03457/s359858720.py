n = int(input())
tl = []
dl = []
flag = 0

for i in range(n):
    t, x, y = (int(x) for x in input().split())
    tl.append(t)
    dl.append((x, y))

for num in range(n):
    if num == 0:
        if tl[num] >= sum(dl[num]) and tl[num] % 2 == sum(dl[num]) % 2:
            pass
        else:
            flag = 1
    else:
        ntl = tl[num]-tl[num-1]
        ndl = sum((abs(dl[num][0] - dl[num - 1][0]), abs(dl[num][1] - dl[num - 1][1])))
        if ntl >= ndl and ntl%2 == ndl%2:
            pass
        else:
            flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")