n, t = map(int, input().split())
a = [int(i) for i in input().split()]
min_a = a[0]
max_a = a[0]
diff = 0
num = 0
for aa in a:
    if min_a > aa:
        min_a = aa
        max_a = aa
    elif min_a < aa:
        if aa - min_a > diff:
            diff = aa - min_a
            num = 1
        elif aa - min_a == diff:
            num += 1
print(num)