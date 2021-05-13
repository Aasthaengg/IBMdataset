def witness(a, n, t, u):
    x = pow(a, u, n)  # x0 = a^u mod nを計算
    
    for _ in range(0, t):
        y = (x * x) % n

        # 法nの下での1の非自明な平方根が存在するのはnが合成数であるときに限る
        if y == 1 and x != 1 and x != (n - 1):
            return True
        x = y
    return y != 1

def is_probably_prime(n, witnesses):
    t = 1
    u = n >> 1
    while u & 1 == 0:
        t = t + 1
        u >>= 1
    assert(2**t * u == n - 1)

    for a in witnesses:
        if a < n and witness(a, n, t, u):
            return False
    return True

def is_definitely_prime(n):
    if ((not (n & 1)) and n != 2) or (n < 2) or ((n % 3 == 0) and (n != 3)):
        return False
    elif n <= 3:
        return True
    else:
        return is_probably_prime(n, [2, 7, 61])

n = int(input())
answer = 0
for _ in range(0, n):
    m = int(input())
    if is_definitely_prime(m):
        answer = answer + 1
print(answer)
