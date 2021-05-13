n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
s, t = 0, 0
x = []
for i in range(n):
    if a[i] < b[i]:
        ans += 1
        s += b[i] - a[i]
    elif a[i] > b[i]:
        x.append(a[i] - b[i])
x.sort(reverse = True)
if s == 0:
    print(0)
    exit()
for i in range(len(x)):
    t += x[i]
    ans += 1
    if s <= t:
        print(ans)
        exit()
print(-1)