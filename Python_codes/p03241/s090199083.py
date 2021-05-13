N,M=list(map(int,input().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
Mdiv = make_divisors(M)
out = 1
for k in Mdiv:
    A = M//k
    if A>=N:
        out = max(out,k)
print(out)
