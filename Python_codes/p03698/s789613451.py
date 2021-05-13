S = input()

l = []

for s in S:
    if s in l:
        print('no')
        exit()
    l.append(s)
print('yes')