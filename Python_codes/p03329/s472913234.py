n = int(input())
def func(n, i):
    ans = 0
    while n>0:
        ans += n%i
        n //= i
    return ans
b=n
for i in range(n+1):
    tmp = func(i, 6) + func(n-i, 9)
    b = min(tmp, b)
print(b)