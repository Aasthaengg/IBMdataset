n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    sum = 0
    tmp = i
    while tmp != 0:
        sum += tmp%10
        tmp = tmp//10
    if sum >= a and sum <= b:
        ans += i
print(ans)