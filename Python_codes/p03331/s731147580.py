n = int(input())

res = 0

while n:
    res += n % 10
    n //= 10
if res == 1:
    print(10)
else:
    print(res)