import itertools

n, a, b = map(int, input().split())

if a > b:
    print(0)
    exit()

if a != b and n == 1:
    print(0)
    exit()

print((b-a)*(n-2)+1)
