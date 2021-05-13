n, m, a, b = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.append(a)
y.append(b)

if max(x) < min(y):
    print('No War')
else:
    print('War')