N = int(input())
t, a = map(int, input().split(' '))

for _ in range(N - 1):
    nt, na = map(int, input().split(' '))
    if nt >= t and na >= a:
        t = nt
        a = na
    else:
        tr = (t + nt - 1) // nt
        ar = (a + na - 1) // na
        r = max(tr, ar)
        t = r * nt
        a = r * na

print(t + a)
