k = int(input())
a, b = map(int, input().split())
print('OK' if sum(i % k == 0 for i in range(a, b + 1)) else 'NG')