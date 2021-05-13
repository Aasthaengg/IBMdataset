n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
if n==1 and t[0] != a[0]:
    print(0)
    exit()
p = [False for i in range(n)]
p[0] = True
p[n - 1] = True

for i in range(1, n):
    if t[i] > t[i - 1]:
        p[i] = True
        if a[i] < t[i]:
            print(0)
            exit()

for i in range(n - 2, -1, -1):
    if a[i] > a[i + 1]:
        p[i] = True
        if t[i] < a[i]:
            print(0)
            exit()
h=[min(t[i],a[i]) for i in range(n)]
mod = 10**9 + 7
total = 1
for i in range(n):
    if not p[i]:
        total = (total * h[i]) % mod
print(total)
