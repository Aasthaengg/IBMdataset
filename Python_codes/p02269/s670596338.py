n = int(input())
data = {}
for _ in range(n):
    key = input()
    if key[0] == 'i':
        data.setdefault(key[7:], '0')
    else:
        if key[5:] in data:
            print('yes')
        else:
            print('no')
