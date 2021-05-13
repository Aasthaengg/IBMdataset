N = int(input())
v = list(map(int, input().split()))

v.sort()

value = v[0]

for n in range(1,N):
    value = (value + v[n]) / 2

print(value)