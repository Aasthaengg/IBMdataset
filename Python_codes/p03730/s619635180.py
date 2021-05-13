A,B,C = map(int,input().split())
ls = [A,B]
ls.sort()
rm = ls[0]
while rm != 0:
    rma = rm
    rm = ls[1] % rm
if C%rma == 0:
    print('YES')
else:
    print('NO')