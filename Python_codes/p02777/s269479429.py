s, t = input().split()
a, b = list(map(int, input().split()))
u = input()
if s == u:
    print('{} {}'.format(a - 1, b))
else:
    print('{} {}'.format(a, b - 1))
