N = int(input())
table = [0]*(N+2)
def factorize2(n): # 素因数分解　2次元素数リスト([素数,指数])
    i = 2
    m = 1
    
    sign = -1
    while i * i <= n:
        j = 0
        while n % i == 0:
            n //= i
            j += 1
        if j != 0:
            table[i] += j
        if i >= 5:
            if sign < 0:
                sign = 1
                i = 6*m + sign
            else:
                m += 1
                sign = -1
                i = 6*m + sign
        elif i == 2:
            i += 1
        elif i == 3:
            i = 5
    if n > 1:
        table[n] += 1
    return table # list


for i in range(2,N+1):
    factorize2(i)
ans = 1
for i in range(len(table)):
    if table[i] > 0:
        ans *= table[i]+1
        ans %= 10**9+7

print(ans)
