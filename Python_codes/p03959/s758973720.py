mo = 1000000007
n = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))

if n == 1:
    if t[0] == a[0]:
        print(1)
    else:
        print(0)
    exit()

mt = [False] * n # 山の高さが1通りのときTrue
mt[0] = True
mt[-1] = True

for i in range(1, n):
    if t[i - 1] < t[i]:
        mt[i] = True
        if a[i] < t[i]:
            print(0)
            exit()

for i in range(n - 2, -1, -1):
    if a[i] > a[i + 1]:
        mt[i] = True
        if t[i] < a[i]:
            print(0)
            exit()

ans = 1
for i in range(n):
    if not mt[i]:
        ans *= min(t[i], a[i])
        ans %= mo

print(ans)
