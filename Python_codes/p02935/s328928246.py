N = int(input())
v = sorted(list(map(float, input().split())))

for i in range(N - 1):
    v1 = v.pop(0)
    v2 = v.pop(0)
    v.append((v1 + v2) / 2)
    v.sort()
print(v[0])
