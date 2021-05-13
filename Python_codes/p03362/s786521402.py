N = int(input())

def sieve(n):
    res = [True for _ in range(n + 1)]
    res[0] = False
    res[1] = False
    i = 2
    while i * i <= n:
        if res[i]:
            for j in range(i * 2, n + 1, i):
                res[j] = False
        i += 1
    return res

S = sieve(55555)
A = []
cnt = 0

for i in range(55555):
    if S[i] and i % 5 == 1:
        A.append(i)
        cnt += 1
    if cnt == N:
        break

print(*A)