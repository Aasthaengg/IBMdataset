x = [int(i) for i in input().split()]
s = '1974'
import sys
for i in x:
    if str(i) not in s:
        print('NO')
        sys.exit()
print('YES') if sum(x) == 21 else print('NO')
