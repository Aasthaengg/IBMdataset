s = str(input())
if s == 'RRR':
    print(int(3))
elif s == 'SSS':
    print(int(0))
elif s == 'RRS' or s == 'SRR':
    print(int(2))
else:
    print(int(1))