K = int(input())
A = [int(_) for _ in input().split()]
l = r = 2
for a in A[::-1]:
    l = a * ((l - 1) // a) + a
    r = a * (r // a + 1) - 1
for x in [l, r]:
    for a in A:
        x = a * (x // a)
    if x != 2:
        print(-1)
        exit()
print(l, r)
