# coding = SJIS

n = int(input())
a = [int(input()) for i in range(n)]
ans = 0

a.sort()

i = 0

while i < n:
    ko = 1
    while (i + ko) < n and a[i] == a[i + ko]:
        ko += 1
    if ko % 2 == 1:
        ans += 1
    i += ko

print(ans)