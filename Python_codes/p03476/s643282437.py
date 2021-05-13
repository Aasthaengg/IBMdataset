from itertools import accumulate


def eratos(N):
    is_prime = [1]*(N+1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            for j in range(i**2, N+1, i):
                is_prime[j] = 0
    return is_prime


inf = 10**5
is_prime = eratos(inf)
like_2007 = [0]*(inf+1)
for i in range(1, inf+1):
    if is_prime[i] == 1 and i % 2 == 1:
        if is_prime[(i+1)//2]:
            like_2007[i] = 1
cumsum = list(accumulate(like_2007))
# print(like_2007)
# print(cumsum)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r]-cumsum[l-1])
