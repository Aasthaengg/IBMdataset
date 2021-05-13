N = int(input())
a = list(map(int, input().split()))

av = sum(a) / N
mi = 101
c = 0
for i in range(N - 1, -1, -1):
    if abs(a[i] - av) <= mi:
        mi = abs(a[i] - av)
        idx = i
print(idx)
