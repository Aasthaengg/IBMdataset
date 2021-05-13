n = int(input())
dishes = []
for _ in range(n):
    a, b = map(int, input().split())
    dishes.append((a+b, a, b))

dishes.sort(key=lambda x: -x[0])

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += dishes[i][1]
    else:
        ans -= dishes[i][2]

print(ans)