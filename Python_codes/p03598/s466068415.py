n = int(input())
k = int(input())
x = list(map(int, input().split()))

res = 0
for v in x:
    res += 2 * min(v, k - v)

print(res)