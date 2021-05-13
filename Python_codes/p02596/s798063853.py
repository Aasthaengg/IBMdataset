K = int(input())

if K % 7 == 0:
    K //= 7

L = 9 * K

if L % 2 == 0 or L % 5 == 0:
    ans = -1
else:
    ans = 0
    R = 10
    while 1:
        ans += 1
        if R % L == 1:
            break
        else:
            R = (10 * R) % L

print(ans)