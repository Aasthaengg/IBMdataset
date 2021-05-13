def check(i):
    print(i)
    c[i] = input()
    if c[i] == 'Vacant':
        exit(0)
n = int(input())
c = [-1]*n
l = 0
r = n-1
check(l)
check(r)
while True:
    m = (l+r)//2
    check(m)
    if (c[l] == c[m] and (m-l) % 2 != 0) or (c[l] != c[m] and (m-l) % 2 == 0):
        r = m
    else:
        l = m