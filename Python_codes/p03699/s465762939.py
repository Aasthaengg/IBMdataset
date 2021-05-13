n = int(input())
point_t = []
f = []
ans = 0
index_0 = 0
cnt = 0
sum_of_0 = 0

for _ in range(n):
    point_t.append(int(input()))

point = sorted(point_t)

for i in range(n):
    if point[i]%10 != 0:
        if cnt == 0:
            index_0 = i
            cnt += 1
        f.append(int(point[i]%10))
if sum(f) == 0:
    print(0)
elif sum(f)%10 != 0:
    for i in range(n):
        ans += int(point[i])
    print(ans)
else:
    print(sum(point) - point[index_0])