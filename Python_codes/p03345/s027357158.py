a, b, c, k = map(int, input().split())
if abs(a-b) > 10**18:
    print('Unfair')
    exit()
if k % 2 == 0:
    print(a-b)
else:
    print((a-b)*(-1))