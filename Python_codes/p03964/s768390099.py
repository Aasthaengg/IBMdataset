N = int(input())

t, a = map(int, input().split())

for i in range(N - 1):
    nt, na = map(int, input().split())
    p = max(t // nt, a // na)
    pt = nt * p
    pa = na * p
    while pt < t or pa < a:
        pt += nt
        pa += na
    t = pt
    a = pa
print(t + a)
