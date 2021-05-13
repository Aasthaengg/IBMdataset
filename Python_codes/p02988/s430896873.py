n = int(input())
p = list(map(int, input().split()))

ans = 0
sanko = []
ssanko = []
for i in range(1, n-1):
    sanko = [p[i-1], p[i], p[i+1]]
    ssanko = sorted(sanko)
    if sanko[1] == ssanko[1]:
        ans += 1
print(ans)
