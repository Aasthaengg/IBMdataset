n = int(input())
a = sorted(list(map(int, input().strip().split())))
print(a[-1] - a[0])