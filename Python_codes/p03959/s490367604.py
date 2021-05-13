n = int(input())

t = list(map(int, input().split()))
a = list(map(int, input().split()))

MOD = 10 ** 9 + 7

if max(t) != max(a):
    print(0)
    exit()

if n == 1:
    print(1)
    exit()

ans = 1
for i in range(1, n - 1):
    if t[i] != t[i - 1]:
        if a[i] < t[i]:
            print(0)
            exit()
    elif a[i] != a[i + 1]:
        if t[i] < a[i]:
            print(0)
            exit()
    else:
        ans *= min(a[i], t[i])
        ans %= MOD

print(ans)

