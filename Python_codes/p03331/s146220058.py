N = int(input())

n = 1
ans = 10**5

def calucurate(M):
    n = 0
    while M > 0:
        n += M%10
        M //= 10
    return n

while n < N:
    t = N - n
    m = calucurate(t) + calucurate(n)
    ans = min(ans,m)
    n += 1

print(ans)