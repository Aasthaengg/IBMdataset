n = int(input())
s = input()

if n % 2 == 1:
    print('No')
    exit(0)

n = n // 2
a = s[:n]
if s.count(a) == 2:
    print('Yes')
else:
    print('No')