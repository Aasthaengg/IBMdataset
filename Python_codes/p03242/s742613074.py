N = list(input())
M = []
for i in N:
    if i == '1':
        M.append('9')
    else:
        M.append('1')

print(''.join(M))