n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
l = []
for x, y in zip(v, c):
    l.append(x-y)
ans = 0
for num in l:
    if num > 0:
        ans += num
print(ans)