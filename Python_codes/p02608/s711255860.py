n = int(input())
a = [0] * (n + 1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            c = x * x + y * y + z * z + x * y + y * z + z * x
            if c <= n:
                a[c] +=1
            else:
                break
for i in a[1:]:
    print(i)
