n = int(input())
x = input()

def count(n):
    cnt = 0
    while n:
        cnt += n % 2
        n //= 2
    return cnt

LIMIT = 5*10**5
dp = [0] * LIMIT
for i in range(1, LIMIT):
    dp[i] = dp[i % count(i)]+1

c = x.count("1")
a = int(x,2) % (c+1)

if c == 1:
    for i in range(n):
        if x[i] == "0":
            print(dp[(a + pow(2, n-i-1, c+1)) % (c+1)] + 1)
        else:
            print(0)
    exit()

b = int(x,2) % (c-1)
for i in range(n):
    if x[i] == "0":
        print(dp[(a + pow(2, n-i-1, c + 1)) % (c + 1)] + 1)
    else:
        print(dp[(b - pow(2, n-i-1, c - 1)) % (c - 1)] + 1)
