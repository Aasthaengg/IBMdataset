n = int(input())
a = list(map(int, input().split()))

ave = sum(a) / n
d = 200
ans = 0
for i, f in enumerate(a):
    if d > abs(ave - f):
        d = abs(ave - f)
        ans = i

print(ans)
