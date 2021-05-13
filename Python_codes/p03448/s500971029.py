five_h = int(input())
one_h = int(input())
f_m = int(input())
s = int(input())

count = 0

for i in range(0, five_h + 1):
    a = 500 * i
    b = 0
    for j in range(0, one_h + 1):
        b = 100 * j
        d = 0
        c = a + b
        for k in range(0, f_m + 1):
            d = 50 * k
            e = c + d
            if e == s:
                count += 1

print(count)