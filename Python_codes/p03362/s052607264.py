import numpy as np
N = int(input())

U = 55556
is_prime = np.full(U+1, True)
is_prime[:2] = False
for p in range(2, U+1):
    if p*p > U:
        break
    if is_prime[p]:
        is_prime[p*p::p] = False


ans = []
i = 2
while len(ans) < N and i < 55556:
    if i % 5 == 1 and is_prime[i] == True:
        ans.append(i)
    i += 1
print(*ans)
