n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
MOD = 10**9 + 7

li_t = []
max_t = 0
for i in range(n):
    if t[i] > max_t:
        li_t.append((t[i], t[i] + 1))
        max_t = t[i]
    else:
        li_t.append((1, max_t + 1))

li_a = []
max_a = 0
for i in range(n)[::-1]:
    if a[i] > max_a:
        li_a.append((a[i], a[i] + 1))
        max_a = a[i]
    else:
        li_a.append((1, max_a + 1))
li_a = li_a[::-1]

ans = 1
for i in range(n):
    tmp = min(li_t[i][1], li_a[i][1]) - max(li_t[i][0], li_a[i][0])
    if tmp <= 0:
        ans *= 0
    ans *= tmp
    ans %= MOD
print(ans)