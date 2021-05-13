x = int(input())
a = x // 11
x -= a * 11
if x == 0:
    print(2 * a)
elif x <= 6:
    print(2 * a + 1)
else:
    print(2 * a + 2)