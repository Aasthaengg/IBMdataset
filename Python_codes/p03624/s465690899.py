S = sorted(set(input()))
A = 'abcdefghijklmnopqrstuvwxyz'

for a in A:
    if a not in S:
        print(a)
        exit()
print('None')