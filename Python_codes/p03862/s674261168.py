n, x = map(int, input().split())
l = [int(i)for i in input().split()]
last = 0
z = 0
for n in l:
    if n + last > x:
        z += n + last - x
        last = x - last
    else:
        last = n
print(z)
