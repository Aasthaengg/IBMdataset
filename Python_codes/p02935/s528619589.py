N = int(input())
v = list(map(int, input().split()))

v.sort()

for i in range(N - 1):
    temp = (v[0] + v[1]) / 2
    v = v[2:]
    v.append(temp)
    v.sort()

print(v[0])