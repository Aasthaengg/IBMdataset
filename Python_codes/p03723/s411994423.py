a, b, c = map(int, input().split())

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and a == b == c:
    print(-1)
    exit()

ans = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    a_tmp = b // 2 + c // 2
    b_tmp = a // 2 + c // 2
    c_tmp = a // 2 + b // 2
    a, b, c = a_tmp, b_tmp, c_tmp
    ans += 1

print(ans)