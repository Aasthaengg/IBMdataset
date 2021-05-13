k, x = map(int, input().split())
dif = k - 1
if dif == 0:
    print(x)
else:
    mini = x - dif
    maxi = x + dif
    a = []
    for i in range(mini, maxi + 1):
        a.append(str(i))
    s = ' '.join(a)
    print(s)