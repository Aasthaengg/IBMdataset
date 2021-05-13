a, b, c = map(int, input().split())
ans = 0
lst = sorted([a, b, c])
while not lst[0]==lst[1]==lst[2]:
    ans += 1
    if lst[0] == lst[1]:
        lst[0] += 1
        lst[1] += 1
    elif lst[1] == lst[2]:
        if lst[2]-lst[0] >= 2:
            lst[0] += 2
        else:
            lst[1] += 1
            lst[2] += 1
    else:
        lst[0] += 2
        lst.sort()

print(ans)