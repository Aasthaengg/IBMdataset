def compare(a, b, c):
    if a < b and b < c:
        print('Yes')
    else:
        print('No')

a, b, c = [int(x) for x in input().split()]
compare(a, b, c)