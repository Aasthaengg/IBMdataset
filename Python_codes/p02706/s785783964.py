n, m = map(int, input().split())
list01 = input().split()
list02 = [int(a) for a in list01]
if sum(list02) <= n:
    print(n - sum(list02))
else:
    print('-1')