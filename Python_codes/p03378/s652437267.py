n, m, x = map(int, input().split())
a = list(map(int, input().split()))

to_z, to_n = 0, 0
for i in a:
    if i > x:  to_n += 1
    else:  to_z += 1

print(min(to_z, to_n))
