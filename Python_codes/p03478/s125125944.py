n, a, b = list(map(int, input().split()))
ans = 0

for i in range(1,n+1):
    m = str(i)
    x = len(m)
    cnt = 0
    for j in range(x):
        cnt = cnt + int(m[j])
    if a <= cnt <= b:
        ans = ans + i
    else:
        continue
print(ans)