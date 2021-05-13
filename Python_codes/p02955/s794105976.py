def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

def checker(A,k):
    A.sort(reverse=True)
    if sum(A[sum(A) // d:]) <= k:
        return True
    return False

n,k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for d in make_divisors(sum(A)):
    buf = []
    for a in A:
        buf.append(a%d)
    #print(buf)
    if checker(buf,k):
        print(d)
        break