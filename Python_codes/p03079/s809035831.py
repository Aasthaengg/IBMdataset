a, b, c = [int(I) for I in input().split()]
print('YNeos'[not(a == b and b == c)::2])
