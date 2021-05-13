X, N = map(int, input().split())
p = list(map(int, input().split()))
s = set(p)
d = 10**18
ans = 0

for i in range(-1000, 1000):
    if i not in s and abs(X-i)<d:
        d = abs(X-i)
        ans = i

print(ans)