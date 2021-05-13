n = int(input())
s = set()
for _ in range(n):
    i = input()
    if i[0] == 'i':
        s |= {i[7:]}
    else:
        if i[5:] in s:
            print('yes')
        else:
            print('no')

