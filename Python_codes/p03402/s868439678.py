import math
b, a = map(int, input().strip().split(" "))
h = 2 * math.ceil(max((a - 1) / 25, (b - 1) / 25)) + 1
a -= 1
b -= 1
print("{} {}".format(h, 100))
for i in range(h):
    if i % 2 == 0:
        print("." * 50 + "#" * 50)
    else:
        if a > 0 and b > 0:
            ma = min(a, 25)
            mb = min(b, 25)
            print("#." * ma + "##" * (25 - ma) + "#." * mb + "##" * (25 - mb))
            a -= ma
            b -= mb
        elif a == 0 and b > 0:
            mb = min(b, 25)
            print("." * 50 + "#." * mb + "##" * (25 - mb))
            b -= mb
        elif a > 0 and b == 0:
            ma = min(a, 25)
            print("#." * ma + "##" * (25 - ma) + "#" * 50)
            a -= ma
