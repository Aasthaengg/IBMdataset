N = int(input())
v = sorted(map(int, input().split()), reverse=True)

for _ in range(N - 1):
    v.append((v.pop(-1) + v.pop(-1)) / 2)

print(v[0])