n, k = map(int, input().split())

if k % 2 == 0:
    step = k // 2
    a = step
else:
    step = k
    a = step

ans = 0

while a <= n:
    b_num = c_num = (n+a)//k - a//k
    ans += b_num * c_num

    a += step

print(ans)
