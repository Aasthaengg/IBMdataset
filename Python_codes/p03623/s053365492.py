n, a, b = map(int, input().split())
if min(abs(n-a), abs(n-b)) == abs(n-a):
    print('A')
else:
    print('B')