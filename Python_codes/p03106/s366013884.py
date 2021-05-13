def dv(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
A,B,K = map(int,input().split())
C = list(set(dv(A))&set(dv(B)))
C.sort()
C.reverse()
print(C[K-1])