N, x = map(int, input().split())
a = list(map(int, input().split()))
a_min = sorted(a)
temp = 0
count = 0
for i in range(N):
    temp += a_min[i]
    if temp > x:
        break
    count += 1
print(count - 1 if temp < x else count)