def query(i):
    print(i)
    return input()


n = int(input())
gender = query(0)
if gender == 'Vacant':
    exit()
l = 0
r = n
for _ in range(19):
    mid = (l + r) // 2
    res = query(mid)
    if res == 'Vacant':
        exit()
    cnt = mid - l + 1
    if (cnt % 2 == 0 and res == gender) or (cnt % 2 != 0 and res != gender):
        r = mid
    else:
        l = mid
        gender = res