n, k = map(int, input().split())
a = list(map(int, input().split()))
l = len(bin(k))-2
if k == 0:
    l = 0
memo = [0 for i in range(l)]

for ai in a:
    for j in range(l):
        if ai & (1<<j):
            memo[j] += 1

x = 0
f = 0

for j in reversed(range(l)):
    if f or k & (1<<j):
        if memo[j] <= n - memo[j]:
            x += 2 ** j
        else:
            f = 1
ans = 0

for ai in a:
    ans += ai ^ x

print(ans)