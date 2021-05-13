N = int(input())
v = list(map(int, input().split()))

v.sort()
ans = 0

for i in range(N - 1):
    v1 = v.pop(0)
    v2 = v.pop(0)
    vv = (v1 + v2) / 2
    v.insert(0, vv)
print(v[0])