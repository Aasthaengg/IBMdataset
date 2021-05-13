n = int(input())
a = [int(input()) for _ in range(n)]
print('first' if any(a[i]%2 == 1 for i in range(n)) else 'second')
