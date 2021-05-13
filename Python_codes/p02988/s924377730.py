n = int(input())
p = list(map(int, input().split()))
res = 0
for i in range(1, len(p) - 1):
    if min(p[i - 1], p[i], p[i + 1]) != p[i] and max(p[i - 1], p[i], p[i + 1]) != p[i]:
        res += 1
print(res)
