n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

is_ok_a = [False] * n
max_a = [0]*n
pre = -1
for i, j in enumerate(a):
    if j != pre:
        pre = j
        is_ok_a[i] = True
    max_a[i] = pre

is_ok_b = [False] * n
max_b = [0]*n
pre = -1
for i, j in reversed(list(enumerate(b))):
    if j != pre:
        pre = j
        is_ok_b[i] = True
    max_b[i] = pre
mod = 10**9+7
ans = 1
for i in range(n):
    if is_ok_a[i] and is_ok_b[i]:
        if max_a[i] == max_b[i]:
            ans *= 1
        else:
            ans *= 0
    elif is_ok_a[i]:
        if max_a[i] <= max_b[i]:
            ans *= 1
        else:
            ans *= 0
    elif is_ok_b[i]:
        if max_a[i] >= max_b[i]:
            ans *= 1
        else:
            ans *= 0
    else:
        ans *= min(max_a[i], max_b[i])
    ans %= mod
print(ans)
