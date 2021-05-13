N = int(input())

a = list(map(int, input().split()))

goke = 0
ans = 0

for i in range(len(a)):
    goke += a[i]

ave = goke / N

ans = 0
for i in range(len(a)):
    if abs(ave-a[ans]) > abs(ave - a[i]):
        ans = i


print(ans)