n = int(input())
t = 1
d = 10**9+7
for i in range(1, n+1):
    t = t * i % d
print(t)