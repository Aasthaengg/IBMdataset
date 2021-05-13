n = int(input())
a = [int(input()) for _ in range(n)]

print('first' if any(x % 2 for x in a) else 'second')