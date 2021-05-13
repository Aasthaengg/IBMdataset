N = int(input())

FACTOR = 10 ** 9 + 7

num = 1
for i in range(1, N+1):
    num *= i
    k, r = divmod(num, FACTOR)
    num = r

print(r)