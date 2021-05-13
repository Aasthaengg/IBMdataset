
n = int(input())

ans = 0

l = [int(x) for x in list(str(n))]
ans = sum(l)

if ans % 9 == 0:
    print('Yes')
else:
    print('No')