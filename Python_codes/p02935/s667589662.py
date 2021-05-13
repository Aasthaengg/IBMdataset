n = int(input())
v = list(map(int ,input().split()))

t = 0
num = 0
v.sort()
for i in range(n):
    if i == 0:
        num += v[0]
    else:
        t = v[i]
        num = (num+t)/2

print(num)