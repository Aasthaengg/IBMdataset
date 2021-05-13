n = input().split()

n_i = [int(s) for s in n]

a, b, c = n_i

if (b-a == c-b):
    print('YES')
else:
    print('NO')