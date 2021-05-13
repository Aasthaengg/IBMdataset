a, b = map(int, input().split())
c = int(str(a) + str(b))
div_c = int(c ** 0.5)
if div_c**2 == c:
    print('Yes')
else:
    print('No')