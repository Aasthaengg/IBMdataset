n = input()

res = 0

for e in n:
    res += int(e)

if res % 9 == 0:
    print('Yes')
else:
    print('No')
