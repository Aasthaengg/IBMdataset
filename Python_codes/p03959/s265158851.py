n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

# 解説AC
if n <= 2:
    print(int(t == a))
    exit()

ans = 1
for i in range(1, n - 1):
    ht, ha = 0, 0
    if t[i - 1] < t[i] and a[i] > a[i + 1]:
        if t[i] != a[i]:
            print(0)
            break
    if t[i - 1] < t[i]:
        if t[i] > a[i]:
            print(0)
            break
    elif a[i] > a[i + 1]:
        if t[i] < a[i]:
            print(0)
            break
    else:
        ans = ans * min(t[i], a[i]) % mod
else:
    print(ans)
