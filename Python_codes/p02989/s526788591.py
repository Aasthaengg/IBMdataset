n = int(input())
a = sorted(map(int, input().split()))
print(a[n // 2] - a[n // 2 - 1])