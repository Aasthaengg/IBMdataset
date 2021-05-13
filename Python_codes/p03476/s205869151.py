def eratosthenes(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0], is_prime[1] = False, False
    prime = []
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return prime
    

Q = int(input())
N = 10**5

prime = eratosthenes(N)
prime_num = [0 for i in range(N+1)]
for p in prime:
    prime_num[p] = 1
    
count = 0
ans = [0 for i in range(N+1)]
for i in range(1, N+1, 2):
    if prime_num[i] == 1 and prime_num[(i+1)//2] == 1:
        count += 1
    ans[i] = count
    
for i in range(Q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l-2])