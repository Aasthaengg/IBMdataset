s = int(input())
l, r = 1, int(1e9)
while l+1 < r:
    m = l+r >> 1
    if m*m <= s:
        l = m
    else:
        r = m
print(0, 0, r, 1, r*r-s, r)