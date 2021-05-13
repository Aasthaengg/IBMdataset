import bisect
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
point = bisect.bisect_right(a, 0)
a_minus = a[:point]
a_plus = a[point:]
len_plus = len(a_plus)
if (len(a_minus) > 0) & (len(a_plus) > 0):
    ans = sum(a_plus) - sum(a_minus)
    print(ans)
    for i in range(len(a_plus)):
        if len_plus == 1:
            x = a_plus.pop(0)
            y = a_minus.pop(0)
            print(str(x) + " " + str(y))
        elif (i == 0):
            x = a_minus.pop(0)
            y = a_plus.pop(0)
            print(str(x) + " " + str(y))
        elif i == len_plus - 1:
            y = x - y
            x = a_plus.pop(0)
            print(str(x) + " " + str(y))
        else:
            x = x - y
            y = a_plus.pop(0)
            print(str(x) + " " + str(y))
    for j in range(len(a_minus)):
        x = x - y
        y = a_minus.pop(0)
        print(str(x) + ' ' + str(y))
elif len(a_plus) > 0:
    ans = sum(a_plus) - ((a[0]) * 2)
    print(ans)
    for i in range(len(a_plus) - 1):
        if i == 0:
            x = a_plus.pop(0)
            y = a_plus.pop(0)
            print(str(x) + " " + str(y))
        elif i == len_plus - 2:
            y = x - y
            x = a_plus.pop(0)
            print(str(x) + " " + str(y))
        else:
            x = x - y
            y = a_plus.pop(0)
            print(str(x) + " " + str(y))
elif len(a_minus) > 0:
    ans = (a_minus[-1] * 2) - sum(a_minus)
    print(ans)
    for i in range(len(a_minus) - 1):
        if i == 0:
            x = a_minus[-1]
            y = a_minus.pop(0)
            print(str(x) + " " + str(y))
        elif i == len_plus - 2:
            x = x - y
            y = a_minus.pop(0)
            print(str(x) + " " + str(y))
        else:
            x = x - y
            y = a_minus.pop(0)
            print(str(x) + " " + str(y))