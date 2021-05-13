from math import log2

N = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(len(a)):
    tmp = a[i]
    while a[i]%2 != 1:
        if a[i]%2 == 0:
            ans += 1
            a[i] /= 2
print(ans)
