x, n = map(int, input().split())
if n != 0:
    l = list(map(int, input().split()))
else:
    l = []

diff = 10**10
ans = 10**10

for i in range(102):
    if i in l:
        continue
    else:
        if abs(x-i) < diff:
            ans = i
            diff = abs(x-i)

print(ans)
