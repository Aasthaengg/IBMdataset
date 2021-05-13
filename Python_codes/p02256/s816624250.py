x, y = map(int, input().split())

if x > y:
    larger = x
    smaller = y
else:
    larger = y
    smaller = x

while True:
    quot, rem = divmod(larger, smaller)  # a > b ?????????
    larger = smaller
    smaller = rem
    if rem == 0:
        gcd = larger
        break

print(gcd)

pass