n = int(input())
a = sorted(list(map(int, input().split())))
print("Yes" if sum(a[:-1]) > a[-1] else "No")