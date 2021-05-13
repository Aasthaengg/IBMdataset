h, n = map(int,input().split())
a = list(map(int,input().split()))

sum_a = sum(a)

if sum_a < h:
    print('No')
else:
    print('Yes')
