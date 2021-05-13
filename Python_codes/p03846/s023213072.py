mod = 10 ** 9 + 7
n = int(input())
a_i = list(map(int, input().split()))
a_i.sort()
ans = 1
if max(a_i) >= n: ans = 0
else:
    for x in range(n //2):
        if n % 2 == 0:
            if a_i[2 * x] != 2 * x + 1 or a_i[2 * x + 1] != 2 * x + 1: ans = 0
            else: 
                ans *= 2
                ans = ans % mod
        elif a_i[0] == 0 and n % 2 != 0:
            if a_i[2 * (x + 1) - 1] != 2 * (x + 1) or a_i[2 * (x + 1)] != 2 * (x + 1): ans = 0
            else: 
                ans *= 2
                ans = ans % mod
        else: ans = 0
print(ans % mod)