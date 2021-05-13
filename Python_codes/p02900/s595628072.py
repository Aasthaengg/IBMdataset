A, B = map(int, input().split())

def prime_factor(n):
    res = set([1])
    for i in range(2, n + 1):
        if i * i > n:
            break
            
        while n % i == 0:
            res.add(i)
            n //= i
            
    if n != 1:
        res.add(n)
        
    return res

print(len(prime_factor(A) & prime_factor(B)))
