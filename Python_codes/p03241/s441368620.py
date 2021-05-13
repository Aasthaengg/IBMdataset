def resolve():
    N, M = list(map(int, input().split()))
    factors = []
    i = 1
    while i <= M**(1/2):
        if M%i==0:
            factors.append(i)
            factors.append(M//i)
        i += 1
    factors = sorted(factors, reverse=True)
    #print(factors)
    for fac in factors:
        if N*fac <= M and (M-N*fac)%fac == 0:
            print(fac)
            break


if '__main__' == __name__:
    resolve()