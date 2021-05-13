n = int(input())
a = sorted(map(int, input().split()))

acc = 0
ans = 0

for i in range(n):
    if acc * 2 >= a[i]:
        ans += 1
    else:
        ans = 1
    acc += a[i]

print(ans)

