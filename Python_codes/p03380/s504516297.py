n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
check = a[-1] / 2
MIN = 10 ** 10

for i in range(n - 1):
    if abs(a[i] - check) < MIN:
        keep = i
        MIN = abs(a[i] - check)

print(a[-1], a[keep])
