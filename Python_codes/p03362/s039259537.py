N=int(input())
MAX = 55555*5 + 10
def makePrimeChecker(n):
    """
    エラトステネスの篩.
    nまでの自然数が素数かどうかを表すリストを返す.
    O(nloglog(n))
    """
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i*i, n+1, i): #i 毎に大きくする
                isPrime[j] = False
    return isPrime

is_prime = makePrimeChecker(MAX)
nums = []
for num in range(2, 55555+1):
    if is_prime[num]:
        if num % 5 == 1:
            nums.append(num)
ans = nums[:N]
print(*ans)