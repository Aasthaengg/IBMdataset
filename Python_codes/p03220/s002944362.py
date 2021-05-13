n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = -1
nearest = 10**18
for i in range(n):
    target = t - h[i] * 0.006  # まさかのこれ（アホか？
    if abs(a - nearest) > abs(a - target):
        nearest = target
        ans = i + 1
print(ans)
