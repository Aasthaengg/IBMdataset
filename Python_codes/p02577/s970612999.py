n = str(input())

count = 0
for v in list(n):
    count += int(v)

if (count % 9) == 0:
    print('Yes')
else:
    print('No')
