n = int(input())

a = tuple(map(int, input().split()))

ans = 0

for j in range(61):
    one = 0
    zero = 0
    for i in a:
        if (i >> j) & 1 == 1:
            one += 1
        else:
            zero += 1
    ans += one*zero*2**j
    ans %= 10**9 + 7

print(ans)