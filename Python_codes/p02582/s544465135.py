s = input()
if s == 'RRR':
    print(3)
elif s in ('RRS', 'SRR'):
    print(2)
elif s == 'SSS':
    print(0)
else:
    print(1)