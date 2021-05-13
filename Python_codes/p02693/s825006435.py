target = int(input())
a, b = map(int, input().split())

b_largest = (b // target) * target

print('OK' if b_largest >= a else 'NG')

