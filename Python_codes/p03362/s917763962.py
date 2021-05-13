# 0からnまでの値が素数かどうかの、len=n+1のリストを作った後に、それを使ってn以下の素数のリストを作成
def primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5) + 1):
        # 既にfalseになってたらスキップ
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

n = int(input())
ans_ls = [0] * n
i = 0
for prime in primes(55555):
    if prime % 5 == 1:
        ans_ls[i] = prime
        i += 1
        if i == n:
            break
print(*ans_ls)