N = int(input())

candidates = [True]*(2*(10**5)+1)
candidates[0] = candidates[1] = False

for i in range(2, N):
    for j in range(i, 2*(10**5)+1, i):
        candidates[j] = False

for n, n_is_prime in enumerate(candidates):
    if n_is_prime:
        print(n)
        break