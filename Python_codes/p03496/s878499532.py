import bisect, copy

n = int(input())
a = list(map(int, input().split()))
b = copy.copy(a)
ans = []
num = 1
count = 0
while num != n:
    if max(a) < 0:
        break
    while a[num - 1] > a[num]:
        a2 = copy.copy(a)
        a2.sort()
        temp = a[num - 1] - a[num]
        temp2 = bisect.bisect_left(a2, temp)
        if temp2 == n:
            temp2 -= 1
        ans.append([a.index(a2[temp2]) + 1, num + 1])
        a[num] += a2[temp2]
        count += 1
        if count == n * 2 + 1:
            break
    num += 1
    if count == n * 2 + 1:
        break

ans2 = []
num = n - 2
count2 = 0
while num != -1:
    if min(b) > 0:
        break
    while b[num] > b[num + 1]:
        b2 = copy.copy(b)
        b2.sort()
        temp = b[num + 1] - b[num]
        temp2 = bisect.bisect_right(b2, temp)
        if temp2 == 0:
            temp2 += 1
        ans2.append([b.index(b2[temp2 - 1]) + 1, num + 1])
        b[num] += b2[temp2 - 1]
        count2 += 1
        if count2 == n * 2 + 1:
            break
    num -= 1
    if count2 == n * 2 + 1:
        break

if len(ans) == 0 and len(ans2) == 0:
    print(0)
elif len(ans) == 0:
    print(len(ans2))
    for i in ans2:
        print(i[0], i[1])
elif len(ans2) == 0:
    print(len(ans))
    for i in ans:
        print(i[0], i[1])
else:
    if len(ans) > len(ans2):
        print(len(ans2))
        for i in ans2:
            print(i[0], i[1])
    else:
        print(len(ans))
        for i in ans:
            print(i[0], i[1])