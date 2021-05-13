n = int(input())
a = sorted([int(input()) for _ in range(n)])
print(sum(a[:-1])+a[-1]//2)
