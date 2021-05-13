# D - Partition
import bisect
N, M = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n,0.5)+1)):
        if n%i==0:
            divisors.append(i)
            if i!=n//i: 
                divisors.append(n//i)
    divisors.sort()
    return divisors

d = make_divisors(M)
print(M//d[bisect.bisect_left(d, N)])
