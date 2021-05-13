def prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

Q = int(input())
LR = [list(map(int,input().split())) for _ in range(Q)]
p = prime_list(100010)
s = []
s.append(0)
for i in range(100001):
    if (i%2 == 1) and i in p and (i+1)//2 in p:
        s.append(s[i]+1)
    else:
        s.append(s[i])
for lr in LR:
    print(s[lr[1]+1]-s[lr[0]])