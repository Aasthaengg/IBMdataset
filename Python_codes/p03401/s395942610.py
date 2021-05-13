n = int(input())
a = [0] + list(map(int, input().split())) + [0]
d = []

for i in range(n + 1):
    d.append(abs(a[i] - a[i + 1]))

ref = sum(d)

for i in range(1, n + 1):
    ans = ref - sum(d[i - 1: i + 1]) + abs(a[i - 1] - a[i + 1])
    print(ans)