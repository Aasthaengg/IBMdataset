n, a, b = map(int, input().split())

ans = 0
sum = 0
for i in range(1, n+1):
    q = len(str(i))
    for j in range(q):
        sum += int(str(i)[j])
    if sum >= a and sum <= b:
        ans += i
    sum = 0
print(ans)
