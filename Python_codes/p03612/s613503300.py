n = int(input())
Ps = list(map(int, input().split()))

prev = False
ans = 0
for i in range(n):
    if Ps[i] == i+1:
        ans += 1
        if prev:
            ans -= 1
            prev = False
        else:
            prev = True
        continue
    prev = False
print(ans)
