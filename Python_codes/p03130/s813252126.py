import sys
a = list(map(int, input().split()))
a += list(map(int, input().split()))
a += list(map(int, input().split()))

for i in [1, 2, 3, 4]:
    if 1 <= a.count(i) <= 2:
        continue
    else:
        print('NO')
        sys.exit()
print('YES')
