n,m = map(int, input().split())
l = list(map(int, input().split()))
a = sum(l)

if a > n:
    print('-1')
else:
    print(n - a)