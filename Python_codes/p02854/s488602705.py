n = int(input())
a = list(map(int, input().split()))
t = sum(a)
b = 0

for i in range(n):
    b += a[i]
    tmp = abs(2*b-t)
    ans = tmp if i==0 else min(ans, tmp)

print(ans)