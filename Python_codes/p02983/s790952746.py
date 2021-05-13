l, r = map(int, input().split())
d = (r -l)%2019
if r -l >=2018:
    print(0)
    exit(0)
ans = 2018
for i in range(l, l+d):
    for j in range(i+1, l+d+1):
        if (i*j)%2019 < ans:
            ans =(i*j)%2019
print(ans)