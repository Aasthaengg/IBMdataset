n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
p = 10 ** 8
ans = 0
for i in range(n):
    x = t - h[i] * 0.006
    x = abs(a - x)
    if p > x:
        p = x
        ans = i + 1
print(ans)