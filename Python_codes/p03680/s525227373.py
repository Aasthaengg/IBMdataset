n = int(input())
l = [int(input()) for _ in range(n)]
ans = 1
num = l[0]
for i in range(n):
    if num == 2:
        break
    num = l[num-1]
    ans += 1
if num == 2:
    print(ans)
else:
    print(-1)