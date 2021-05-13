N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for i in arr:
    if i % 2 == 1:
        ans += 1
if ans % 2 == 1:
    print('NO')
else:
    print('YES')