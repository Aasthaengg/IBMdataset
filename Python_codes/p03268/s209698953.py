n, k = map(int, input().split())
count0, count1 = 0, 0

for i in range(1, n+1):
    if i%k == 0:
        count0 += 1
    elif i%k == k/2:
        count1 += 1
ans = count0**3
if k%2 == 0:
    ans += count1**3
print(ans)
