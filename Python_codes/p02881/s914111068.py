def divisors(n):
    divs = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divs.append((i, n//i))
        i += 1
    return divs

def resolve():
    N = int(input())
    factors = divisors(N)
    ans = float("inf")
    for x, y in factors:
        ans = min(ans, (x-1)+(y-1))
    print(ans)
    

    
if '__main__' == __name__:
    resolve()