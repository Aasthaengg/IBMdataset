a, b = input().split()
if b == 'D':
    if a == 'H':
        a = 'D'
    else:
        a = 'H'
elif a == b == 'D':
    a = 'H'

print(a)