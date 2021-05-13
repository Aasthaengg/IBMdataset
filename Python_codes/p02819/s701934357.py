def erathosthenes(n):
    if n < 2:
        return False
    
    prime_list = []
    search_max = n ** 0.5

    cand = [i for i in range(2, n+1)]
    while True:
        prime_cand = cand[0]
        if search_max <= prime_cand:
            return prime_list + cand
        prime_list.append(prime_cand)
        cand = [j for j in cand if j % prime_cand != 0]

X = int(input())
SIZE = 100003
prime_list = erathosthenes(SIZE)

for i in range(len(prime_list)):
    if prime_list[i] >= X:
        print(prime_list[i])
        break