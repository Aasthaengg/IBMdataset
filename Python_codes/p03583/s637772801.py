N = int(input())

def f(n):
    res = []
    i = 1
    while i <= n**0.5:
        if n%i == 0:
            res.append(n)
            if N//i > i:
                res.append(N//i)
        i += 1
    return res

num = 4
if N%4 == 0:
    num = 1
    N //= 4
elif N%2 == 0:
    num = 2
    N //= 2

P = f(N)
P.sort(reverse=True)
ans = []
for p in P:
    i = 1
    while p*i <= 3500:
        Q = f(N//p)
        for q in Q:
            j = 1
            while q*j <= 3500:
                if num*p*i*q*j-(p*i+q*j)*N > 0 and ((p*i)*(q*j)*N)%(num*p*i*q*j-(p*i+q*j)*N) == 0:
                    ans = [p*i, q*j, ((p*i)*(q*j)*N)//(num*p*i*q*j-(p*i+q*j)*N)]
                    i = 4000
                    j = 4000
                j += 1
            if len(ans) > 0:
                break
        i += 1
    if len(ans) > 0:
        break

print(*ans)