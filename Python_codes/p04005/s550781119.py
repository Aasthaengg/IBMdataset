l = [int(x) for x in input().split()]

l.sort(reverse=True)


if len([x for x in l if x % 2 == 0]) > 0:
    print(0)
else:
    ans = min(l[1]*l[2], l[0]*l[1], l[0]*l[2])
    print(ans)