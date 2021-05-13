n = int(input())
i = str(n)
m = n // 100
if str(m) == i[-1]:
    print('Yes')
else:
    print('No')