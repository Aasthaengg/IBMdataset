h,a = [int(x) for x in input().split()]

if h % a == 0:
    print(h//a)
else:
    print(h//a + 1)