def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:continue
        for j in range(i * 2, n + 1, i):is_prime[j] = False
    return is_prime

def main():
    q=int(input())
    is_prime = primes(10**5+1)
    a = [0 for i in range(10**5+1)]
    for i in range(3,10**5+1):
        if is_prime[i] and is_prime[(i+1)//2]:a[i]+=1
    for i in range(3,10**5+1):a[i]+=a[i-1]
    for i in range(q):
        l,r=map(int,input().split())
        print(a[r]-a[l-1])

main()
