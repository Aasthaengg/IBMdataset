n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

mod = 10 ** 9 + 7

yama = [0] * n

# tは、t[i] == t[i + 1]だったら左の以外全部ありうる
yama[0] = t[0]
if t[0] > a[0]:
    print(0)
    exit()
for i in range(n - 1):
    if t[i] < t[i + 1]:
        # i + 1の高さ確定
        yama[i + 1] = t[i + 1]
        if t[i + 1] > a[i + 1]:
            print(0)
            exit()
for i in range(n - 1, 0, -1):
    if a[i - 1] > a[i]:
        yama[i - 1] = a[i - 1]
        if a[i - 1] > t[i - 1]:
            print(0)
            exit()
if a[n - 1] > t[n - 1]:
    print(0)
    exit()
yama[n - 1] = a[n - 1]

ans = 1
for i in range(1, n - 1):
    if yama[i] == 0:
        ans = (ans * min(a[i], t[i])) % mod
print(ans)
