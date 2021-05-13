q = int(input())
is_prime = [1] * (10**5 + 1)
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, 10**5+1):
    if is_prime[i] == 1:
        for j in range(i+i, 10**5+1, i):
            is_prime[j] = 0
ls = [0]
for i in range(1, 10**5+1):
    if is_prime[i] == 1 and is_prime[(i+1)//2] == 1:
        ls.append(ls[i-1]+1)
    else:
        ls.append(ls[i-1])
for i in range(q):
    l, r = map(int, input().split())
    print(ls[r] - ls[l-1])
