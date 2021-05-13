n = int(input())
alst = list(map(int, input().split()))
ans = 0
ave = sum(alst) / n
d = abs(ave - alst[0])

for i, num in enumerate(alst):
    d_tmp = abs(ave - num)
    if d_tmp < d:
        ans = i
        d = d_tmp
print(ans)