S = set(input())
alp = 'abcdefghijklmnopqrstuvwxyz'

for a in alp:
    if not a in S:
        print(a)
        break
else:
    print('None')