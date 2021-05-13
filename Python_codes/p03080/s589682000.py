n = int(input())
s = sorted(input())
check_num = n//2 - 1 if n % 2 == 0 else n//2

if s[check_num] == 'R':
    print('Yes')
else:
    print('No')
