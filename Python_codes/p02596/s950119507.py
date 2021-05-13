K = int(input())

if K % 7 == 0:
    K //= 7

L = 9 * K

ans = -1

r = 10

for i in range(L):
    r %= L
    if r == 1:
        ans = i + 1
        break
    else:
        r = 10 * r

print(ans)