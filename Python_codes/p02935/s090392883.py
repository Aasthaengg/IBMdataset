n = int(input())
v = list(map(int,input().split()))

v.sort()
for i in range(n-1):
    if i == 0:
        t = (v[i] + v[i+1]) / 2
    else:
        t = (t + v[i+1]) / 2

print(t)

