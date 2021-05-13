A,B,K = map(int,input().split())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
    
lstA = make_divisors(A)
lstB = make_divisors(B)
#print(lstA,lstB)
fin = []

for i in lstA:
    if i in lstB:
        fin.append(i)
#print(fin)
fin.sort(reverse = True)
print(fin[K-1])
