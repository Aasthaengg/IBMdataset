n, k = map(int, input().split())
a = list(map(int, input().split()))
right = 0
left = 0

for i in range(n):
    cnt_left = 0
    cnt_right = 0
    for j in range(n):
        if a[i] > a[j]:
            if i < j:
                cnt_right += 1
            elif i > j:
                cnt_left += 1
    right += cnt_right % (10 ** 9 + 7)
    left += cnt_left % (10 ** 9 + 7)
    cnt_right = 0
    cnt_left = 0

ans = ((right * k) % (10 ** 9 + 7)) + (right + left) * ((k * (k - 1) // 2) % (10 ** 9 + 7))
ans = ans  % (10 ** 9 + 7)

print(ans)