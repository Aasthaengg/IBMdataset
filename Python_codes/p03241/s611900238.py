N,M=map(int, input().split())
#均等に配分したい
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

D=make_divisors(M)
D=sorted(D)
ans=0
for d in D:
    if M//d>=N:
        ans=d
print(ans)
