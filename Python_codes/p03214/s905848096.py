n = int(input())
a = list(map(int, input().split()))
ave = sum(a) / n

ans = -1
dif = 10000
for i, ai in enumerate(a):
    d = abs(ai-ave)
    if d < dif:
        dif = d
        ans = i
print(ans)
