s = set(input())
alp = 'abcdefghijklmnopqrstuvwxyz'
for a in alp:
    if a not in s:
        print(a)
        exit()
print('None')