S, T = [x for x in input().split()]

A, B = [int(x) for x in input().split()]

U = input()

if S == U:
    A -= 1
else:
    B -= 1

print('{} {}'.format(A, B))
