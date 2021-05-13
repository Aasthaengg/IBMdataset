N, T = map(int, input().split())
A = list(map(int, input().split()))

m = 10**9+1
s = 0
c = 0
for a in A:
    m = min(m, a)
    if a - m > s:
        s = a - m
        c = 1
    elif a - m == s:
        c += 1

print(c)