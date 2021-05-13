A, B, C, D = map(int, input().split())

a, m = divmod(A, D)
if m > 0:
    a += 1

b, m = divmod(C, B)
if m > 0:
    b += 1

print('Yes' if a >= b else 'No')
