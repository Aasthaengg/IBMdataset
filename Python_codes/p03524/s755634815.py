s = input()
l = [s.count(i) for i in 'abc']
if max(l)-min(l)<=1:
    print('YES')
else:
    print('NO')