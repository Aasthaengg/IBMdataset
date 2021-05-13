x = int(input())
a, b = map(int, input().split())
print((b // x) * x >= a and "OK" or "NG")