n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
now = 0
kari = []
ans = 0
for i in range(n):
    if a[i] < b[i]:
        ans += 1
        now += b[i]-a[i]
    elif a[i] >= b[i]:
        kari.append(a[i] - b[i])
kari.sort(reverse=True)
for i in kari:
    if now > 0:
        now -= i
        ans += 1
    elif now <= 0:
        break
if now > 0:
    print(-1)
elif now <= 0:
    print(ans)