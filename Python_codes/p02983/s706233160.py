l,r = map(int, input().split())
ans = 2019

for i in range(l, min(l+2019, r)):
    for j in range(i+1, min(l+2019, r+1)):
        a = (i * j) % 2019
        ans = min(ans, a)

print(ans)
