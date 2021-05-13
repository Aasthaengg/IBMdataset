import math

N = int(input()) * 3
a = list(map(int, input().split()))
ans = 0

a = sorted(a, reverse = True)

for i in range(1, int(2.0 / 3.0 * float(N)), 2):
    #print(a[i])
    ans += a[i]

print(ans)