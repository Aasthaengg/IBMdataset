def end():
    print(0)
    exit()

mod = 10**9+7
n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
t1 = [0]*n
a1 = [0]*n
t1[0] = a1[-1] = 1

for i in range(1, n):
    if t[i-1] != t[i]:
        t1[i] = 1
    if a[n-1-i] != a[n-i]:
        a1[n-1-i] = 1

ans = 1
for i in range(n):
    if t1[i] and a1[i]:
        if t[i] != a[i]:
            end()
    elif t1[i]:
        if t[i] > a[i]:
            end()
    elif a1[i]:
        if t[i] < a[i]:
            end()
    else:
        ans *= min(t[i], a[i])
        ans %= mod
print(ans)