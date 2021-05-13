l, r = map(int, input().split())
if r-l >=2020:
    print(0)
    exit()
ans = 2018
for i in range(l, r+1):
    for j in range(l, r+1):
        if i != j:
            a = i*j%2019
            ans = min(ans, a)
print(ans)