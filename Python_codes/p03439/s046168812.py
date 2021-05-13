N = int(input())

lst = [-1] * N

r = 0
print (r)
s = str(input())
if s == 'Vacant':
    exit()
elif s == 'Male':
    lst[r] = 1
else:
    lst[r] = 0

l = N - 1

print (l)
s = str(input())
if s == 'Vacant':
    exit()
elif s == 'Male':
    lst[l] = 1
else:
    lst[l] = 0


# print (r, l)
while True:
    mid = (l + r) // 2
    print (mid)
    s = str(input())
    if s == 'Vacant':
        exit()
    elif s == 'Male':
        lst[mid] = 1
    else:
        lst[mid] = 0

    if (mid - r) % 2 == 0: #間が奇数個
        if lst[r] == lst[mid]: #この間に空席がない可能性あり
            r = mid
        else:
            l = mid
    else: #間が偶数個
        if lst[r] == lst[mid]: #この間に空席がない可能性あり
            l = mid
        else:
            r = mid

    # print (r, l)