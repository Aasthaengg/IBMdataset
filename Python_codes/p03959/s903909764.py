n = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
k = [-1 for i in range(n)]
now = 0
if t[-1] != a[0]:
    print(0)
    exit()
for i in range(n):
    if t[i] > now:
        k[i] = t[i]
        now = t[i]

now = 0
for i in reversed(range(n)):
    if k[i] == -1:
        if a[i] > now:
            k[i] = a[i]
            now = a[i]
    if k[i] != -1:
        if a[i] > now:
            now = a[i]
        if k[i] > now:
            print(0)
            exit()

ans = 1
l = 0
cou = 0
mod = 10**9 + 7
for i in range(n):
    if k[i] != -1 and l == 0:
        l = k[i]
    elif k[i] != -1 and l != 0:
        ans *= pow(min(l,k[i]),cou,mod)
        ans %= mod
        l = k[i]
        cou = 0
    elif k[i] == -1:
        cou += 1
print(ans)