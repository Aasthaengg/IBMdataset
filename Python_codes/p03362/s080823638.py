import sys

N = int(sys.stdin.readline().rstrip())


import math

def sieve_of_eratosthenes(n):
    prime_list = []  # n以下の素数のリスト
    A = [1]*(n+1)    # A[i] = iが素数なら1,その他は0
    A[0] = A[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if A[i]:
            prime_list.append(i)
            for j in range(i**2,n+1,i):
                A[j] = 0
    for i in range(math.floor(math.sqrt(n))+1,n+1):
        if A[i] == 1:
            prime_list.append(i)
    return prime_list


prime_list = sieve_of_eratosthenes(1361)

ANS = [2]
for p in prime_list:
    if p == 2:
        continue
    else:
        if p % 10 == 1:
            ANS.append(p)
            if len(ANS) == N:
                break

print(*ANS)