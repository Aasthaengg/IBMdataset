n = list(input())
i = 0

while i < 3:
    if n[i] == '1':
        n[i] = '9'
        i = i + 1
    else:
        n[i] = '1'
        i = i + 1

print(''.join(n))