m = 10**9 + 7
n = int(input())
t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
h = [t[i] if i == 0 or t[i-1] < t[i] else a[i] if i == n - 1 or a[i] > a[i+1] else -1
     for i in range(n)]
ans = 1
top = 0
for i in range(n):
    top = max(top, h[i])
    ans *= 1 if top == t[i] else 0
top = 0
for i in reversed(range(n)):
    top = max(top, h[i])
    ans *= 1 if top == a[i] else 0
prev = 0
for i in range(1, n):
    if h[i] > 0:
        ans = ans * pow(min(h[prev], h[i]), i - prev - 1, m) % m
        prev = i
print(ans)