n = int(input())
s = input().split()
a = [0]*4

for i in s:
    if i == 'P':
        a[0] += 1
    elif i == 'W':
        a[1] += 1
    elif i == 'G':
        a[2] += 1
    elif i == 'Y':
        a[3] += 1

if a.count(0) == 0:
    print('Four')
else:
    print('Three')