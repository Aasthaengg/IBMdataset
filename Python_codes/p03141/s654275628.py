n = int(input())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, -b, a+b))
li.sort(key=lambda x:-x[2])
ans = 0
for i in range(n):
    ans += li[i][i%2]
print(ans)