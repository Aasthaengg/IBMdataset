n, *a_l = map(int, open(0).read().split())
before = a_l[0]
not_decrease, not_increase = False, False
cnt = 1
for a in a_l:
    if not_decrease:
        if before > a:
            cnt += 1
            not_decrease = False
    elif not_increase:
        if before < a:
            cnt += 1
            not_increase = False
    else:
        if before == a:
            continue
        elif before < a:
            not_decrease = True
        else:
            not_increase = True
    before = a
print(cnt)