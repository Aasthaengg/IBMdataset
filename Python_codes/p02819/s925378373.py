def make_prime_checker(n):
    # nまでの自然数が素数かどうかを表すリストを返す  O(nloglogn)
    is_prime = [False, True, False, False, False, True] * (n//6+1)
    del is_prime[n+1:]
    is_prime[1:4] = False, True, True
    for i in range(5, int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * (n//i-i+1)
    return is_prime

P = make_prime_checker(101010)
X = int(input())
for i in range(X, 101010):
    if P[i]:
        print(i)
        exit()
