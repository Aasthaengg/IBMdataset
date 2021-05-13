a = [int(s) for s in input().split()]
b = input()
c = list(b)
c[a[1] - 1] = c[a[1] - 1].lower()
print(''.join(c))