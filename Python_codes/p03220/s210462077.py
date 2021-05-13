n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
l = a + 10000

for i in range(n):
    k = abs(t-h[i]*0.006-a)
    if l > k:
        l = k
        ans = i+1

print(ans)