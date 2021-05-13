def digitsum(n):
    tmp = 0
    while n > 0:
        tmp += n % 10
        n //= 10
    return tmp


N = int(input())
m = 10**5+1
for i in range(1, N//2+1):
    A = digitsum(i)
    B = digitsum(N-i)
    m = min(m, A+B)
print(str(m))