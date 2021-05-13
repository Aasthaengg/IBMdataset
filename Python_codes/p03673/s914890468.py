n = int(input())
a = [int(i) for i in input().split()]

if n % 2 == 0:
    lis1 = a[::2]
    lis2 = a[::-2]
    ans = lis2 + lis1
else:
    lis1 = a[::-2]
    lis2 = a[1::2]
    ans = lis1 + lis2
ans = map(str, ans)
print(' '.join(ans))