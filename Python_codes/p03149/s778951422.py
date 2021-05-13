check = [1,9,7,4]

n1,n2,n3,n4 = map(int,input().split())

if n1 in check:
    check.remove(n1)
if n2 in check:
    check.remove(n2)
if n3 in check:
    check.remove(n3)
if n4 in check:
    check.remove(n4)

if len(check) == 0:
    print('YES')
else:
    print('NO')