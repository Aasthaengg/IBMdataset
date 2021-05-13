n = int(input())
v = list(map(int, input().split()))
v.sort()
s = 0
temp = v[0]
for i in range(n - 1):
    s = (temp + v[i + 1]) / 2
    temp = s
print(s)
