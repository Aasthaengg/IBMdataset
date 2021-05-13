n = int(input())
a = list(map(int, input().split()))

a.sort()

# lに個数を格納
l = []
i = 0
num = 1
while True:
    while i+1 < n and a[i] == a[i+1]:
        i += 1
        num += 1
    l.append(num)
    num = 1
    i += 1
    if i == n:
        break

ans = len(l)
num = 0
for i in l:
    if i % 2 == 0:
        num += 1
if num % 2 == 1:
    ans -= 1
print(ans)