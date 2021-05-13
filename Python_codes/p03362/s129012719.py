def primes(n):
    i = 1
    p = [2]
    while i+2 <= n:
        flag = True
        i += 2
        for j in range(3, int(i**(1/2))+1, 2):
            if i % j == 0:
                flag = False
                break
        if flag:
            p.append(i)
    return p
n = int(input())
l = primes(55555)
l = [i for i in l if i % 5 == 1]
print(*l[:n])