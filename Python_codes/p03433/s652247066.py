N = int(input())
a = int(input())

q, r = divmod(N, 500)

if r <= a:
    print('Yes')
else:
    print('No')