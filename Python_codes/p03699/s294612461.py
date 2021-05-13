n = int(input())
s = []
smallest = 1000

flag = True
for i in range(n):
    val = int(input())
    s.append(val)

    if (val % 10) > 0:
        flag = False
        if val < smallest:
            smallest = val

if flag:
    print(0)
else:
    total = sum(s)
    if (total % 10) == 0:
        print(total - smallest)
    else:
        print(total)