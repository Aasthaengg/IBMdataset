n = int(input())
a = list(map(int, input().split()))
b = [0] * n
cnt = 0
cnt_0 = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
    elif a[i] == 0:
        cnt_0 += 1
    b[i] = abs(a[i])

if cnt % 2 == 0 or cnt_0 >= 1:
    ans = sum(b)
else:
    ans = sum(b) - min(b) * 2

print(ans)