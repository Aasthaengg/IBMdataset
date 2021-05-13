n = int(input())
l = 0
r = n - 1
print(l)
s_l = str(input())
if s_l == 'Vacant':
    exit()
while abs(l - r) > 1:
    m = (l + r) // 2
    print(m)
    s_m = str(input())
    if s_m == 'Vacant':
        exit()
    else:
        if (m - l) % 2:
            if s_m != s_l:
                l = m
                s_l = s_m
            else:
                r = m
                s_r = s_m
        else:
            if s_m != s_l:
                r = m
                s_r = s_m
            else:
                l = m
                s_l = s_m
else:
    print(r)
    s = str(input())
