# 素数判定 O(√N)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def Eratosthenes_sieve(n):
    table = [True]*(n+1)
    for i in range(n+1):
        if is_prime(i):
            for j in range(2*i,n+1,i): # 素数の倍数は非素数
                table[j] = False
        else:
            table[i] = False
    return table

a = 55555
t = Eratosthenes_sieve(a)

N = int(input())
ans = []
for i in range(1,55556,5):
    if t[i]:
        ans.append(i)
ans = ans[:N]
print(*ans)