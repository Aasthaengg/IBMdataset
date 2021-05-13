N = int(input())

t, a = map(int, input().split())

for i in range(N - 1):
    nt, na = map(int, input().split())
    p = max((t + nt - 1) // nt, (a + na - 1) // na)
    t = nt * p
    a = na * p
print(t + a)
