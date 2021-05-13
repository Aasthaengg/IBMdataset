n = int(input())
inter = []
for i in range(n):
    a, b = map(int, input().split())
    inter.append([a-b, a+b])
inter = sorted(inter, key=lambda x: x[1])
ans = 1
rmost = inter[0][1]
for i in range(1, n):
    if inter[i][0] >= rmost:
        rmost = inter[i][1]
        ans+=1
print(ans)

