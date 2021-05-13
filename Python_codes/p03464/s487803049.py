K = int(input())
A = [int(i) for i in input().split()]

A.reverse()

mi, ma = 2, 2

for a in A:
    if ma < ((mi + a - 1) // a) * a:
        print(-1)
        exit()
    mi = (mi + a - 1) // a * a
    ma = (ma // a + 1) * a - 1

print(mi, ma)