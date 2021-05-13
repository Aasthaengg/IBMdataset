n, k = map(int, input().split())
summ = n + k
if summ % 2 != 0:
    print('IMPOSSIBLE')
else:
    print(summ//2)