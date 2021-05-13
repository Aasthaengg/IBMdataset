q = int(input())

lr = [list(map(int, input().split())) for _ in range(q)]

def primes(n):
    # 1であれば素数であるリスト
    primes = [1] * (n+1)
    primes[0] = 0
    primes[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if not primes[i]:
            continue
        for j in range(i * 2, n + 1, i):
            primes[j] = 0
    return primes

MAX = 100000
prime_list = primes(MAX)

# 2017に似た数値かどうかを求めるための累積和用のリスト作成
ans_list = [0] * (MAX + 1)
now = 0
for i in range(MAX):
    if prime_list[i] == 1 and prime_list[(i+1)//2] == 1:
        now += 1
    ans_list[i+1] = now

for i in range(q):
    print(ans_list[lr[i][1]+1] - ans_list[lr[i][0]])