n, m = map(int, input().split())
point = [0] * m
ans = 0
for i in range(n) :
    data = list(map(int, input().split()))
    for j in range(1,data[0]+1) :
        point[data[j]-1] += 1
for k in range(m) :
    if point[k] == n :
        ans += 1
print(ans)
