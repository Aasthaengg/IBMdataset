n, l = list(map(int, input().split()))
total = 0
for i in range(1, n+1):
    total += l+i-1

m = 1000000000
ans = 0
for i in range(1, n+1):
    a = total-(l+i-1)
    # print(a)
    if abs(total-a) < m:
        m = abs(total-a)
        ans = a

print(ans)
